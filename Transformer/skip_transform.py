from Transformer.base_transform import Transformer
from copy import copy

class Skip_Transform(Transformer):
   def __init__(self, operation_dict) -> None:
       super().__init__(operation_dict)
       self.skip_value = operation_dict['count'] 


   def apply(self, document):
      cursor = document.cursor

      if cursor + self.skip_value >= len(document):
         raise ValueError("Skipping past end of document")

      new_document = copy(document)
      new_document.cursor += self.skip_value
      return new_document

