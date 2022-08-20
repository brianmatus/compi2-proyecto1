from expressions.expression import Expression
from elements.env import Environment
from elements.value_tuple import ValueTuple
from types.element_type import ElementType
from returns.ast_return import ASTReturn
from types.arithmetic_type import ArithmeticType

import global_config


class Arithmetic(Expression):

    def __init__(self, left: Expression, right: Expression, _type: ArithmeticType, line: int, column: int):
        super().__init__(line, column)
        self.left = left
        self.right = right
        self._type = _type

    def __str__(self):
        return f'Arithmetic({self.left}, {self._type.name}, {self.right}'

    def execute(self, environment: Environment) -> ValueTuple:

        error_msj: str = ""
        left: ValueTuple = self.left.execute(environment)
        right: ValueTuple = self.right.execute(environment)

        match self._type:
            case ArithmeticType.SUM:

                # INT
                if left._type == ElementType.INT and right._type == ElementType.INT:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.INT)
                # FLOAT
                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.FLOAT)

                # &str + String
                if left._type == ElementType.STRING_PRIMITIVE and right._type == ElementType.STRING_CLASS:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.STRING_CLASS)

                # String + &str
                if left._type == ElementType.STRING_CLASS and right._type == ElementType.STRING_PRIMITIVE:
                    return ValueTuple(value=left.value + right.value, _type=ElementType.STRING_CLASS)

                error_msg = f"Operacion Aritmetica SUMA {left._type.name} <-> {right._type.name} es invalida."
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise Exception(error_msg)

            case ArithmeticType.SUB:
                # INT
                if left._type == ElementType.INT and right._type == ElementType.INT:
                    return ValueTuple(value=left.value - right.value, _type=ElementType.INT)
                # FLOAT
                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value - right.value, _type=ElementType.FLOAT)

                error_msg = f"Operacion Aritmetica RESTA {left._type.name} <-> {right._type.name} es invalida."
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise Exception(error_msg)

            case ArithmeticType.MULT:
                # INT
                if left._type == ElementType.INT and right._type == ElementType.INT:
                    return ValueTuple(value=left.value * right.value, _type=ElementType.INT)
                # FLOAT
                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value * right.value, _type=ElementType.FLOAT)

                error_msg = f"Operacion Aritmetica MULTIPLICACION {left._type.name} <-> {right._type.name} es invalida."
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise Exception(error_msg)

            case ArithmeticType.DIV:
                # INT
                if left._type == ElementType.INT and right._type == ElementType.INT:
                    return ValueTuple(value=left.value / right.value, _type=ElementType.FLOAT)
                # FLOAT
                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value / right.value, _type=ElementType.FLOAT)

                error_msg = f"Operacion Aritmetica DIVISION {left._type.name} <-> {right._type.name} es invalida."
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise Exception(error_msg)

            case ArithmeticType.MOD:
                # INT
                if left._type == ElementType.INT and right._type == ElementType.INT:
                    return ValueTuple(value=left.value % right.value, _type=ElementType.INT)
                # FLOAT
                if left._type == ElementType.FLOAT and right._type == ElementType.FLOAT:
                    return ValueTuple(value=left.value % right.value, _type=ElementType.FLOAT)

                error_msg = f"Operacion Aritmetica MODULAR {left._type.name} <-> {right._type.name} es invalida."
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise Exception(error_msg)

            case ArithmeticType.NEG:

                # INT
                if left._type == ElementType.INT:
                    return ValueTuple(value=0-left.value, _type=ElementType.INT)
                # FLOAT
                if left._type == ElementType.FLOAT:
                    return ValueTuple(value=0-left.value, _type=ElementType.FLOAT)

                error_msg = f"Operacion Aritmetica MODULAR {left._type.name} <-> {right._type.name} es invalida."
                global_config.log_semantic_error(error_msg, self.line, self.column)
                raise Exception(error_msg)

            case _:
                print("ERROR??? Unknown arithmetic type?")


    def ast(self) -> ASTReturn:

        if self._type == ArithmeticType.NEG:
            return self.singular_operation_ast()
        return self.two_operation_ast()

    def singular_operation_ast(self) -> ASTReturn:
        father_index: int = global_config.get_unique_number()
        left_ast = self.left.ast()
        result = f'{father_index}[label="ARITHMETIC {self._type.name}"]\n' \
                 f'{left_ast.value}\n' \
                 f'{father_index} -> {left_ast.head_ref}\n'
        return ASTReturn(result, father_index)

    def two_operation_ast(self) -> ASTReturn:
        father_index: int = global_config.get_unique_number()
        left_ast = self.left.ast()
        right_ast = self.right.ast()
        result = f'{father_index}[label="ARITHMETIC {self._type.name}"]\n' \
                 f'{left_ast.value}\n' \
                 f'{father_index} -> {left_ast.head_ref}\n' \
                 f'{right_ast.value}\n' \
                 f'{father_index} -> {right_ast.head_ref}\n'
        return ASTReturn(result, father_index)


