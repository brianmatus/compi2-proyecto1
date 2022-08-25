from typing import List

from returns.exec_return import ExecReturn
from instructions.instruction import Instruction
from element_types.element_type import ElementType
from elements.env import Environment
from expressions.expression import Expression
from elements.value_tuple import ValueTuple
from elements.condition_clause import ConditionClause

from global_config import log_semantic_error
from errors.semantic_error import SemanticError


class Conditional(Instruction):

    def __init__(self, clauses: List[ConditionClause], line: int, column: int):
        super().__init__(line, column)
        self.clauses: List[ConditionClause] = clauses

    def execute(self, env: Environment) -> ExecReturn:
        for clause in self.clauses:

            env.remove_child(clause.environment)
            clause.environment = Environment(env)
            env.children_environment.append(clause.environment)


            # Reached Else Clause
            if (clause.condition is None):
                instruction: Instruction
                for instruction in clause.instructions:
                    result = instruction.execute(clause.environment)
                    if result.propagate_break or result.propagate_continue or result.propagate_method_return:
                        return result

                return ExecReturn(ElementType.BOOL, True, False, False, False)


            result = clause.condition.execute(clause.environment)

            # Clause accepted
            if (result.value is True):
                for instruction in clause.instructions:
                    result = instruction.execute(clause.environment)
                    if result.propagate_break or result.propagate_continue or result.propagate_method_return:
                        return result

                return ExecReturn(ElementType.BOOL, True, False, False, False)

            # No execution
            return ExecReturn(ElementType.BOOL, False, False, False, False)



