from typing import Union

import errors.semantic_error
import global_config
from elements.symbol import Symbol
from elements.element_type import ElementType
from elements.value_tuple import ValueTuple


class Environment:
    def __init__(self, parent_environment):

        self.parent_environment: Environment = parent_environment
        self.symbol_table:dict = {}
        self.children_environment = []

    def save_variable(self, _id: str, _type: ElementType, value, line: int, column: int, is_array: bool):
        the_symbol: Union[Symbol, None]

        if global_config.ALLOW_NESTED_VARIABLE_OVERRIDE:
            the_symbol = self.symbol_table.get(_id)

            if the_symbol is not None:
                error_msg = "Variable <" + _id + "> ya definida en el ambito actual. ALLOW_NESTED_VARIABLE_OVERRIDE="\
                            + global_config.ALLOW_NESTED_VARIABLE_OVERRIDE

                global_config.log_semantic_error(error_msg, line, column)
                raise Exception(error_msg)

        else:
            the_symbol = self.recursive_get(_id)
            if the_symbol is not None:
                error_msg = "Variable <" + _id + "> ya definida en el ambito actual. ALLOW_NESTED_VARIABLE_OVERRIDE="\
                            + global_config.ALLOW_NESTED_VARIABLE_OVERRIDE

                global_config.log_semantic_error(error_msg, line, column)
                raise Exception(error_msg)

        self.symbol_table[_id] = Symbol(value, _id, _type, is_array)

    def set_variable(self, _id: str, result: ValueTuple, line: int, column: int):
        the_symbol: Symbol = self.recursive_get(_id)

        if the_symbol is None:
            error_msg = f'Variable {_id} no esta definida en el ambito actual'
            global_config.log_semantic_error(error_msg, line, column)
            raise errors.semantic_error.SemanticError(error_msg, line, column)

        if the_symbol._type != result._type:
            error_msg = f'Variable {_id} de tipo {the_symbol._type.name} no puede ser asignada valord e tipo {result._type.name}'
            global_config.log_semantic_error(error_msg, line, column)
            raise errors.semantic_error.SemanticError(error_msg, line, column)

        the_symbol.value = result.value

    # TODO set array variable

    def recursive_get(self, _id: str) -> Union[Symbol, None]:
        if self.symbol_table.get(_id is not None):
            return self.symbol_table.get(_id)

        # hit top
        if self.parent_environment is None:
            return None

        return self.parent_environment.recursive_get(_id)


