from returns.exec_return import ExecReturn
from instructions.instruction import Instruction
from elements.env import Environment
from element_types.element_type import ElementType


class Continue(Instruction):
    def __init__(self, line: int, column: int):
        super().__init__(line, column)

    def execute(self, env: Environment) -> ExecReturn:
        return ExecReturn(ElementType.BOOL, True, False, False, False)