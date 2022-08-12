from expressions.expression import Expression
from elements.env import Environment
from elements.value_tuple import ValueTuple
from elements.element_type import ElementType
from elements.ast_return import ASTReturn
from elements.arithmetic_type import ArithmeticType

import main


class Arithmetic(Expression):

    def __init__(self, left: Expression, right: Expression, _type: ArithmeticType, line: int, column: int):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self._type = _type


    def execute(self, environment: Environment) -> ValueTuple:

        error_msj: str = ""
        left: ValueTuple = self.left.execute(environment)
        right: ValueTuple = self.right.execute(environment)

        match self._type:
            case ArithmeticType.SUM:

                # INT
                if left._type == ElementType.INT and right._type == ElementType.INT:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.INT)
                # FLOAT
                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.FLOAT)

                # STRING

                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.FLOAT)