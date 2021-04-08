from json.decoder import JSONDecodeError
from document import Document
from operation import Operation
import json

def isValid(stale, latest, otjson):
   curr_doc = Document(stale)
   final_doc = Document(latest)
   try:
      operations = json.loads(otjson)
   except JSONDecodeError:
      raise TypeError(f"{otjson} not a valid json object")

   for ot in operations:
      try:
         operation = Operation(ot)
         curr_doc = operation.transform(curr_doc)
      except ValueError:
         return False

   return curr_doc == final_doc


assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}]'
) == True

assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 45}, {"op": "delete", "count": 47}]'
) == False

assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'Repl.it uses operational transformations.',
    '[{"op": "skip", "count": 40}, {"op": "delete", "count": 47}, {"op": "skip", "count": 2}]'
) == False

assert isValid(
    'Repl.it uses operational transformations to keep everyone in a multiplayer repl in sync.',
    'We use operational transformations to keep everyone in a multiplayer repl in sync.',
    '[{"op": "delete", "count": 7}, {"op": "insert", "chars": "We"}, {"op": "skip", "count": 4}, {"op": "delete", "count": 1}]'
) == True
