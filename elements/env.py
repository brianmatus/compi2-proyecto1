from typing import Union

import main
from elements.symbol import Symbol
from elements.element_type import ElementType
from expressions.expression import Expression


class Environment:
    def __init__(self, parent_environment):

        self.parent_environment: Environment = parent_environment
        self.symbol_table = {}
        self.children_environment = []

    def save_variable(self, _id: str, _type: ElementType, value, line: int, column: int, is_array: bool):
        the_symbol: Union[Symbol, None]

        if main.ALLOW_NESTED_VARIABLE_OVERRIDE:
            the_symbol = self.symbol_table.get(_id)

            if the_symbol is not None:
                error_msg = "Variable <" + _id + "> ya definida en el ambito actual. ALLOW_NESTED_VARIABLE_OVERRIDE="\
                            + main.ALLOW_NESTED_VARIABLE_OVERRIDE

                main.logSemanticError(error_msg, line, column)
                raise Exception(error_msg)

        else:
            the_symbol = self.recursive_get(_id)
            if the_symbol is not None:
                error_msg = "Variable <" + _id + "> ya definida en el ambito actual. ALLOW_NESTED_VARIABLE_OVERRIDE="\
                            + main.ALLOW_NESTED_VARIABLE_OVERRIDE

                main.logSemanticError(error_msg, line, column)
                raise Exception(error_msg)

    def recursive_get(self, _id: str) -> Union[Symbol, None]:
        if self.symbol_table.get(_id is not None):
            return self.symbol_table.get(_id)

        # hit top
        if self.parent_environment is None:
            return None

        return self.parent_environment.recursive_get(_id)


