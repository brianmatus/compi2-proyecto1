from elements.env import Environment
from elements.element_type import ElementType
from elements.exec_return import ExecReturn
from elements.ast_return import ASTReturn


class Instruction:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

    # Should implement:
    # execute(env: Environment) -> ExecReturn
    # ast() -> ASTReturn

    def execute(self, env: Environment) -> ExecReturn:
        pass

    def ast(self) -> ASTReturn:
        pass




