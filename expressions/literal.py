from expressions.expression import Expression
from elements.env import Environment
from elements.value_tuple import ValueTuple
from types.element_type import ElementType
from returns.ast_return import ASTReturn
import global_config

class Literal(Expression):

    def __init__(self, value, __type: ElementType, line: int, column: int):
        super(Literal, self).__init__(line, column)
        self.value = value
        self.__type = __type

    def execute(self, environment: Environment) -> ValueTuple:
        return ValueTuple(self.value, self.__type)

    def ast(self) -> ASTReturn:
        father_ref = global_config.get_unique_number()
        value_ref = global_config.get_unique_number()

        value = f'{father_ref}[label="LITERAL\\n{self.__type.name}"]\n' \
                f'{value_ref}[label="{self.value}"]\n' \
                f'{father_ref} -> {value_ref}\n'

        return ASTReturn(value=value, head_ref=father_ref)

    def __str__(self):
        return f'LITERAL(val={self.value} type={self.__type})'

