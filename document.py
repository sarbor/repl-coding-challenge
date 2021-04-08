class Document:
   def __init__(self, document, cursor=0) -> None:
      if cursor >= len(document):
         raise ValueError("cursor cannot be greater than length of string")

      self.cursor = cursor
      self.doc = list(document)

   def __eq__(self, o: object) -> bool:
      if isinstance(o, Document):
          return o.doc == self.doc

      return False

   def __len__(self):
      return len(self.doc)

   def __str__(self) -> str:
       return "".join(self.doc)

   def __copy__(self):
      return type(self)(self.doc, self.cursor)