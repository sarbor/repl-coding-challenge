from Transformer.base_transform import Transformer
from copy import copy


class Delete_Transform(Transformer):
   def __init__(self, operation_dict) -> None:
       super().__init__(operation_dict)
       self.delete_count = operation_dict['count']


   def apply(self, document):
      cursor = document.cursor

      if cursor + self.delete_count >= len(document):
         raise ValueError("Cannot delete past end of string")

      new_doc = copy(document)
      new_doc.doc = new_doc.doc[:cursor] + \
          new_doc.doc[cursor + self.delete_count:]

      return new_doc

      

      

