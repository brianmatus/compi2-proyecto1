from expressions.expression import Expression
from elements.env import Environment
from elements.value_tuple import ValueTuple
from element_types.element_type import ElementType
from returns.ast_return import ASTReturn

from elements.array_symbol import ArraySymbol

from global_config import log_semantic_error
from errors.semantic_error import SemanticError


class ArrayReference(Expression):

    def __init__(self, _id: str, indexes: list, line: int, column: int):
        super().__init__(line, column)
        self._id = _id
        self.indexes = indexes

    def execute(self, environment: Environment) -> ValueTuple:
        the_symbol: ArraySymbol = environment.recursive_get(self._id)

        if the_symbol is None:
            print("Variable not defined in scope")
            error_msg = f'Variable {self._id} no esta definida en el ambito actual'
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        dimensions = []

        print(f'Indexes:{self.indexes}')

        index: Expression
        for index in self.indexes:
            result = index.execute(environment)

            if result._type != ElementType.INT or isinstance(result.value, list):
                error_msg = f'El acceso a array debe de ser con tipo entero'
                log_semantic_error(error_msg, self.line, self.column)
                raise SemanticError(error_msg, self.line, self.column)

            dimensions.append(result.value)

        print(f'Evaluated indexes:{dimensions}')
        print(f'Symbol indexes:{the_symbol.dimensions}')

        if len(the_symbol.dimensions.keys()) < len(dimensions):
            error_msg = f'La profundidad del array es menor a la ingresada'
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        returning = the_symbol.value

        for i in range(len(dimensions)):

            print(f"requested:{dimensions[i]} existing:{the_symbol.dimensions[i+1]}")
            if dimensions[i] > the_symbol.dimensions[i+1]:
                error_msg = f'Las dimensiones del array son menores a las ingresadas'
                log_semantic_error(error_msg, self.line, self.column)
                raise SemanticError(error_msg, self.line, self.column)

            returning = returning[dimensions[i]].value

        a = returning

        if isinstance(returning, ValueTuple):
            return returning
        return ValueTuple(_type=the_symbol._type, value=returning)




