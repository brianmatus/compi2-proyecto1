from typing import Union

from elements.ast_return import ASTReturn
from elements.exec_return import ExecReturn
from instructions.instruction import Instruction
from expressions.expression import Expression

from elements.element_type import ElementType
from elements.env import Environment

from global_config import get_unique_number, log_semantic_error

from elements.array_type import ArrayDefType


class ArrayDeclaration(Instruction):

    def __init__(self, _id: str, array_type: ArrayDefType, expression: Union[Expression, None], is_mutable: bool,
                 line: int, column: int):
        self._id = _id
        self.array_type = array_type
        self.dimensions: int = -1
        self.expression = expression
        self.values = []
        self.is_mutable = is_mutable
        super().__init__(line, column)

    def execute(self, env: Environment) -> ExecReturn:

        print("TODO implement array_declaration exeute")
        pass



