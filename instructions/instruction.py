from elements.env import Environment
from elements.element_type import ElementType


class Instruction:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

        # Should implement:
        # execute(env: Environment) -> ExecReturn
        # ast() -> ASTReturn

