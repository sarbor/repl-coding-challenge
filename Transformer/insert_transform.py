from Transformer.base_transform import Transformer
from copy import copy

class Insert_Transform(Transformer):
   def __init__(self, operation_dict) -> None:
       super().__init__(operation_dict)
       self.chars = list(operation_dict['chars'])


   def apply(self, document):
      cursor = document.cursor
      new_doc = copy(document)
      new_doc.doc = new_doc.doc[:cursor] + self.chars + new_doc.doc[cursor:]
      new_doc.cursor += len(self.chars)
      return new_doc
