from elements.value_tuple import ValueTuple
from elements.env import Environment
from returns.ast_return import ASTReturn

class Expression:
    def __init__(self, line: int, column: int):
        self.line = line
        self.column = column

        # Should have execute(environment: Environment) -> ValueTuple
        # Should have ast() -> ASTReturn

    def execute(self, environment: Environment) -> ValueTuple:
        print("ABSTRACT EXPRESSION EXECUTE CALLED, CHECK LMAO")
        return ValueTuple(None, None)

    def ast(self) -> ASTReturn:
        print("ABSTRACT EXPRESSION EXECUTE CALLED, CHECK LMAO")
        return ASTReturn('error super class', -420)
