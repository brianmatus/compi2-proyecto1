from typing import Union, List

from expressions.expression import Expression
from instructions.instruction import Instruction
from elements.env import Environment


class ConditionClause:
    def __init__(self, condition: Union[Expression, None], instructions: List[Instruction], environment: Environment):
        self.condition: Union[Expression, None] = condition
        self.instructions: List[Instruction] = instructions
        self.environment: Environment = environment
