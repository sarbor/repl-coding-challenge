from Transformer.delete_transform import Delete_Transform
from Transformer.skip_transform import Skip_Transform
from Transformer.insert_transform import Insert_Transform


class Operation:
    def __init__(self, operation):
       if "op" not in operation:
           raise ValueError(f'{operation} must have op key')

       self.transformer = Operation.create_transformer(operation)


    def transform(self, document):
        return self.transformer.apply(document)

    def create_transformer(operation):
        op_to_transformer = {"insert": Insert_Transform,
                              "delete": Delete_Transform,
                              "skip": Skip_Transform}
        op_type = operation['op']
        return op_to_transformer[op_type](operation)
        



    
