from typing import List


from errors.semantic_error import SemanticError
import global_config
from instructions.instruction import Instruction
from returns.ast_return import ASTReturn
from returns.exec_return import ExecReturn
from element_types.element_type import ElementType
from elements.env import Environment
from expressions.expression import Expression
from expressions.literal import Literal
from elements.value_tuple import ValueTuple


class PrintLN(Instruction):

    def __init__(self, expr_list, line: int, column: int):
        super().__init__(line, column)
        self.expr_list: List[Expression] = expr_list

    def execute(self, env: Environment) -> ExecReturn:


        if self.expr_list[0]._type is not ElementType.STRING_PRIMITIVE:
            print("println formatter is not string_primitive")
            error_msg = f'El primer argumento de println debería ser un string primitivo'
            global_config.log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        _str: Literal = self.expr_list[0]

        needed = _str.value.count("{}") + _str.value.count("{:?}")
        print(f'{needed} needed values to fill')

        if needed != len(self.expr_list[1:]):
            error_msg = f'La cantidad de elementos de formato y argumentos obtenidos no es la misma'
            global_config.log_semantic_error(error_msg, self.line, self.column)
            raise SemanticError(error_msg, self.line, self.column)

        the_str: str = _str.value

        print(f"str before replacements:{the_str}")

        for arg in self.expr_list[1:]:
            the_arg = arg.execute(env)

            if the_arg._type in [ElementType.INT, ElementType.FLOAT, ElementType.STRING_PRIMITIVE]:
                the_str = the_str.replace("{}", str(the_arg.value), 1)

            # TODO check for array types
        global_config.console_output += the_str + "\n"







    def ast(self) -> ASTReturn:
        pass
