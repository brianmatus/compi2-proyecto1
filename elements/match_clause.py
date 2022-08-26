from typing import Union, List

from expressions.expression import Expression
from instructions.instruction import Instruction
from elements.env import Environment


class MatchClause:
    def __init__(self, condition: Union[List[Expression], None],
                 instructions: List[Instruction], environment: Environment):
        self.condition: List[Expression] = condition
        self.instructions: List[Instruction] = instructions
        self.environment: Environment = environment
