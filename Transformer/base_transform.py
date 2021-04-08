from abc import ABC, abstractmethod

class Transformer(ABC):
   def __init__(self, operation_dict) -> None:
       super().__init__()

   @abstractmethod
   def apply(self, document):
      pass