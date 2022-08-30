import math
from typing import List, Union

import global_config
from errors.semantic_error import SemanticError
from element_types.func_call_arg import FuncCallArg
from expressions.expression import Expression
from elements.env import Environment
from elements.value_tuple import ValueTuple
from element_types.element_type import ElementType
from elements.symbol import Symbol
from elements.array_symbol import ArraySymbol
from expressions.array_reference import ArrayReference
from expressions.variable_ref import VariableReference
import copy

from element_types.logic_type import LogicType
from global_config import log_semantic_error


class ParameterFunctionCallE(Expression):

    def __init__(self, variable_id: Union[Expression, str], function_id: str, params: List[FuncCallArg], line: int, column: int):
        super().__init__(line, column)

        self.variable_id = variable_id
        self.function_id = function_id
        self.params = params


    def execute(self, environment: Environment) -> ValueTuple:

        print("-------------------param func call-------------------")
        # print(self.variable_id)
        # print(self.function_id)
        # print(self.params)

        print(self.variable_id)
        print(type(self.variable_id))

        the_symbol = None

        if isinstance(self.variable_id, ArrayReference):

            print("array reference!")
            result = self.variable_id.execute(environment)
            a = print(global_config.value_tuple_array_to_array(result.value))

            if isinstance(result.value, list):
                the_symbol = ArraySymbol(self.variable_id._id, result._type, self.variable_id.indexes, result.value, True, False)

            else:
                the_symbol = Symbol(self.variable_id._id, result._type, result.value, True, False)

        elif isinstance(self.variable_id, VariableReference):
            the_symbol = environment.recursive_get(self.variable_id._id)

        else:
            the_symbol = environment.recursive_get(self.variable_id)

        if the_symbol is None:
            error_msg = f"No existe una variable con el nombre {self.variable_id}"
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        if isinstance(the_symbol, Symbol):

            # Built in functions
            if self.function_id == "to_string":
                return self.native_to_string(the_symbol)

            if self.function_id == "abs":
                return self.native_abs(the_symbol)

            if self.function_id == "sqrt":
                return self.native_sqrt(the_symbol)

            if self.function_id == "clone":
                return self.native_clone(the_symbol)

        if isinstance(the_symbol, ArraySymbol):
            if self.function_id == "to_string":
                return self.native_to_string(the_symbol)

            if self.function_id == "len":
                return self.native_len(the_symbol)

            if self.function_id == "clone":
                return self.native_array_clone(the_symbol)





        # TODO Check if is struct
        # if if isinstance(the_symbol, struct_symbol):

        # TODO Check if present in struct
        print("missing stuff")
        error_msg = f"Acceso a parametro de variable invalido.."
        log_semantic_error(error_msg, self.line, self.column)
        raise SemanticError(error_msg, self.line, self.column)

    def native_to_string(self, the_symbol) -> ValueTuple:
        allowed_types = [ElementType.INT, ElementType.USIZE, ElementType.FLOAT,
                         ElementType.BOOL, ElementType.CHAR,
                         ElementType.STRING_PRIMITIVE, ElementType.STRING_CLASS]
        if not the_symbol._type in allowed_types:
            error_msg = f".to_string() solo puede ser usado con i64, usize, f64, bool, char, String, &str."
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        return ValueTuple(str(the_symbol.value), ElementType.STRING_CLASS, False)

    def native_abs(self, the_symbol) -> ValueTuple:
        allowed_types = [ElementType.INT, ElementType.FLOAT]
        if not the_symbol._type in allowed_types:
            error_msg = f".native_abs() solo puede ser usado con i64, f64."
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        return ValueTuple(abs(the_symbol.value), the_symbol._type, False)

    def native_sqrt(self, the_symbol) -> ValueTuple:
        allowed_types = [ElementType.INT, ElementType.FLOAT]
        if not the_symbol._type in allowed_types:
            error_msg = f".native_sqrt() solo puede ser usado con i64, f64."
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        return ValueTuple(math.sqrt(the_symbol.value), ElementType.FLOAT, False)

    def native_clone(self, the_symbol) -> ValueTuple:
        allowed_types = [ElementType.INT, ElementType.USIZE, ElementType.FLOAT,
                         ElementType.BOOL, ElementType.CHAR,
                         ElementType.STRING_PRIMITIVE, ElementType.STRING_CLASS]
        if not the_symbol._type in allowed_types:
            error_msg = f".native_sqrt() solo puede ser usado i64, usize, f64, bool, char, String, &str."
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        return ValueTuple(the_symbol.value, the_symbol._type, False)

    def native_array_clone(self, the_symbol) -> ValueTuple:
        allowed_types = [ElementType.INT, ElementType.USIZE, ElementType.FLOAT,
                         ElementType.BOOL, ElementType.CHAR,
                         ElementType.STRING_PRIMITIVE, ElementType.STRING_CLASS]
        if not the_symbol._type in allowed_types:
            error_msg = f".native_sqrt() solo puede ser usado i64, usize, f64, bool, char, String, &str."
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        return ValueTuple(copy.deepcopy(the_symbol.value), the_symbol._type, False)

    def native_len(self, the_symbol) -> ValueTuple:
        allowed_types = [ElementType.INT, ElementType.USIZE, ElementType.FLOAT,
                         ElementType.BOOL, ElementType.CHAR,
                         ElementType.STRING_PRIMITIVE, ElementType.STRING_CLASS]
        if not the_symbol._type in allowed_types:
            error_msg = f".to_string() solo puede ser usado con i64, usize, f64, bool, char, String, &str."
            log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        return ValueTuple(len(the_symbol.value), ElementType.INT, False)
