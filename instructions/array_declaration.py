from typing import Union, Dict, List

from errors.semantic_error import SemanticError
import global_config

from elements.value_tuple import ValueTuple

from returns.exec_return import ExecReturn
from instructions.instruction import Instruction
from expressions.expression import Expression
from expressions.array_expression import ArrayExpression
from element_types.element_type import ElementType

from elements.env import Environment

from element_types.array_def_type import ArrayDefType


class ArrayDeclaration(Instruction):

    def __init__(self, _id: str, array_type: ArrayDefType, expression: Union[ArrayExpression, None], is_mutable: bool,
                 line: int, column: int):
        self._id = _id
        self.array_type = array_type
        self.dimensions: int = -1
        self.expression = expression
        self.values = []
        self.is_mutable = is_mutable
        super().__init__(line, column)

    def execute(self, env: Environment) -> ExecReturn:

        print("TODO implement array_declaration exeute")


        print(f'Is Nested:{self.array_type.is_nested_array}')
        print(self.array_type)

        # Find out what dimension should I be

        level = 1
        sizes = {}
        arr_def_type = self.array_type
        while True:

            the_size = arr_def_type.size_expr.execute(env)
            if the_size._type is not ElementType.INT:
                error_msg = f'Tamaño de array debe ser una expresion entera'
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise SemanticError(error_msg, self.line, self.column)

            sizes[level] = int(the_size.value)

            if not arr_def_type.is_nested_array:
                break

            arr_def_type = arr_def_type.content_type
            level += 1

        print(f"Levels of nesting:{level}")
        print(sizes)




        # Get my supposed values and found out what dimensions it has
        print("Get my supposed values")
        expression_result: ValueTuple = self.expression.execute(env)
        print(expression_result._type)
        print(expression_result.value)
        #
        # e_level = 1
        # e_sizes = {}
        # e_arr_def_type = expression_result.value
        # while True:
        #     e_sizes[e_level] = int(len(e_arr_def_type.value))
        #     if not isinstance(e_arr_def_type.value, list):
        #         break
        #     e_arr_def_type = e_arr_def_type[0]
        #     level += 1
        # print()

        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        r: bool = global_config.match_dimensions(list(sizes.values()), expression_result.value)
        print(f'Match piti god?:{r}')




