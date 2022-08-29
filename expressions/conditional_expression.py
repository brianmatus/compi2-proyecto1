from typing import List

from returns.exec_return import ExecReturn
from instructions.instruction import Instruction
from element_types.element_type import ElementType
from elements.env import Environment
from expressions.expression import Expression
from elements.value_tuple import ValueTuple
from elements.condition_expression_clause import ConditionExpressionClause

from global_config import log_semantic_error
from errors.semantic_error import SemanticError


class ConditionalExpression(Expression):

    def __init__(self, clauses: List[ConditionExpressionClause], line: int, column: int):
        super().__init__(line, column)
        self.clauses: List[ConditionExpressionClause] = clauses
        # print("conditional expression detected")

    def execute(self, environment: Environment) -> ValueTuple:

        r_type = None
        for clause in self.clauses:
            res = clause.expr.execute(environment)
            if r_type is None:
                r_type = res._type

            if res._type != r_type:
                error_msg = f"Todas las expresiones de un match-expr deben devolver el mismo tipo." \
                            f"({res._type} != {r_type})"
                log_semantic_error(error_msg, self.line, self.column)
                raise SemanticError(error_msg, self.line, self.column)

        for clause in self.clauses:
            print("evaluating class")

            environment.remove_child(clause.environment)
            clause.environment = Environment(environment)
            environment.children_environment.append(clause.environment)

            # Reached Else Clause
            if clause.condition is None:
                print("reached else")
                return clause.expr.execute(environment)

            result = clause.condition.execute(clause.environment)

            if result._type is not ElementType.BOOL:
                error_msg = f"La expresión de un if debe ser de tipo booleano." \
                            f"(Se obtuvo {result.value}->{result._type})."
                log_semantic_error(error_msg, self.line, self.column)
                raise SemanticError(error_msg, self.line, self.column)

            # Clause accepted
            if result.value is True:
                return clause.expr.execute(environment)

        # No execution
        return ValueTuple(ElementType.VOID, None, is_mutable=False)
