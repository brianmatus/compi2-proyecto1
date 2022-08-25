from returns.exec_return import ExecReturn
from instructions.instruction import Instruction
from elements.env import Environment
from element_types.element_type import ElementType
from expressions.expression import Expression


class ReturnI(Instruction):
    def __init__(self, expr: Expression, line: int, column: int):
        super().__init__(line, column)
        self.expr = expr

    def execute(self, env: Environment) -> ExecReturn:

        if self.expr is None:
            return ExecReturn(ElementType.VOID, None, True, False, False)

        result = self.expr.execute(env)
        return ExecReturn(result._type, result.value, True, False, False)
