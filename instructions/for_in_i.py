from typing import List, Union

import global_config
from returns.exec_return import ExecReturn
from instructions.instruction import Instruction
from element_types.element_type import ElementType
from elements.env import Environment
from expressions.expression import Expression
# from elements.value_tuple import ValueTuple
from elements.condition_clause import ConditionClause

from global_config import log_semantic_error
from errors.semantic_error import SemanticError


class ForInRanged:
    def __init__(self, a: Expression, b: Expression):
        self.a: Expression = a
        self.b: Expression = b


class ForInI(Instruction):
    def __init__(self, looper: str, range_expr: Union[Expression, ForInRanged], instructions: List[Instruction],
                 line: int, column: int):
        super().__init__(line, column)
        self.looper: str = looper
        self.instructions: List[Instruction] = instructions
        self.range_expr: Union[Expression, ForInRanged] = range_expr
        self.environment = Environment(None)  # default, for compiler to recognize it
        self.intermediate_env = Environment(None)

    def execute(self, env: Environment) -> ExecReturn:

        print("executing for in")

        env.remove_child(self.intermediate_env)
        self.intermediate_env = Environment(env)
        env.children_environment.append(self.environment)


        elements = []
        the_type = None

        # Check range (before looper to determine type

        if isinstance(self.range_expr, ForInRanged):
            a = self.range_expr.a.execute(env)
            b = self.range_expr.b.execute(env)

            if a._type not in [ElementType.INT, ElementType.USIZE] \
                    or b._type not in [ElementType.INT, ElementType.USIZE]:
                error_msg = f"Un rango definido por a..b debe de ser tipo int o usize"
                log_semantic_error(error_msg, self.line, self.column)
                raise SemanticError(error_msg, self.line, self.column)

            elements = [v for v in range(a.value, b.value)]
            the_type = ElementType.INT


        # TODO check if its vector
        else:
            pass
