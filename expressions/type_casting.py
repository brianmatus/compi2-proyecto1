import errors.semantic_error
from expressions.expression import Expression
from elements.env import Environment
from elements.value_tuple import ValueTuple
from element_types.element_type import ElementType

from element_types.logic_type import LogicType
import global_config


class TypeCasting(Expression):

    def __init__(self, cast_to: ElementType, expr: Expression, line: int, column: int):
        super().__init__(line, column)
        self.cast_to: ElementType = cast_to
        self.expr: Expression = expr


    def execute(self, environment: Environment) -> ValueTuple:
        res = self.expr.execute(environment)

        # Same Types
        if res._type == self.cast_to:
            return res

        ##################################################
        # INT TO USIZE
        if res._type == ElementType.INT and self.cast_to == ElementType.USIZE:
            return ValueTuple(res.value, ElementType.USIZE, res.is_mutable)

        # USIZE TO INT
        if res._type == ElementType.USIZE and self.cast_to == ElementType.INT:
            return ValueTuple(res.value, ElementType.INT, res.is_mutable)

        # INT TO FLOAT
        if res._type == ElementType.INT and self.cast_to == ElementType.FLOAT:
            return ValueTuple(res.value, ElementType.FLOAT, res.is_mutable)
        # FLOAT TO INT
        if res._type == ElementType.FLOAT and self.cast_to == ElementType.INT:
            return ValueTuple(res.value, ElementType.INT, res.is_mutable)


        # INT TO BOOL, INVALID, use != 0
        # BOOL TO INT
        if res._type == ElementType.BOOL and self.cast_to == ElementType.INT:
            return ValueTuple(res.value, ElementType.INT, res.is_mutable)


        # INT TO CHAR
        if res._type == ElementType.INT and self.cast_to == ElementType.CHAR:
            return ValueTuple(res.value, ElementType.CHAR, res.is_mutable)
        # CHAR TO INT
        if res._type == ElementType.CHAR and self.cast_to == ElementType.INT:
            return ValueTuple(res.value, ElementType.INT, res.is_mutable)

        # INT TO STRING INVALID, should be done with .to_string()
        # STRING TO INT  INVALID, always invalid? idk

        ##################################################
        #USIZE TO FLOAT
        if res._type == ElementType.USIZE and self.cast_to == ElementType.FLOAT:
            return ValueTuple(res.value, ElementType.FLOAT, res.is_mutable)
        #FLOAT TO USIZE INVALID, cast to i64 before

        # USIZE TO BOOL INVALID, use != 0
        # BOOL TO USIZE
        if res._type == ElementType.BOOL and self.cast_to == ElementType.USIZE:
            return ValueTuple(res.value, ElementType.USIZE, res.is_mutable)

        # USIZE TO CHAR INVALID
        # CHAR TO USIZE
        if res._type == ElementType.CHAR and self.cast_to == ElementType.USIZE:
            return ValueTuple(res.value, ElementType.USIZE, res.is_mutable)



        ##################################################

        # FLOAT TO BOOL INVALID, use != 0
        # BOOL TO FLOAT INVALID, cast to i64 before

        # FLOAT TO CHAR INVALID
        # CHAR TO FLOAT INVALID, cast to i64 before

        ##################################################

        # BOOL TO CHAR INVALID
        # CHAR TO BOOL INVALID



