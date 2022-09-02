from typing import Union, List

from expressions.expression import Expression
from instructions.instruction import Instruction
from elements.env import Environment


class ConditionExpressionClause:
    def __init__(self, condition: Union[Expression, None], instructions: List[Instruction], expr: Expression,
                 environment: Environment):
        self.condition: Expression = condition
        self.expr: Expression = expr
        self.environment: Environment = environment
        self.instructions: List[Instruction] = instructions
