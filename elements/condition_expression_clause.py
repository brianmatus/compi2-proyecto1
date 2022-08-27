from typing import Union

from expressions.expression import Expression
from elements.env import Environment


class ConditionExpressionClause:
    def __init__(self, condition: Union[Expression, None], expr: Expression, environment: Environment):
        self.condition: Expression = condition
        self.expr: Expression = expr
        self.environment: Environment = environment
