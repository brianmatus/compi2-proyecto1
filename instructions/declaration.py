import errors.semantic_error
import global_config
from instructions.instruction import Instruction
from elements.ast_return import ASTReturn
from elements.exec_return import ExecReturn
from elements.element_type import ElementType
from elements.env import Environment
from expressions.expression import Expression
from elements.value_tuple import ValueTuple


class Declaration(Instruction):

    def __init__(self, _id: str, _type: ElementType, expression: Expression, line: int, column: int):
        super().__init__(line, column)
        self._id = _id
        self._type = _type
        self.expression = expression
        print(f'Instance of declaration with type {self._type.name}')

    def execute(self, env: Environment) -> ExecReturn:
        expr: ValueTuple

        # TODO Declaration without assignment, using default values  (not possible? idk
        # if self.expression == None:
        #     match self._type:
        #         case ElementType.INT:
        #             env.

        expr: ValueTuple = self.expression.execute(env)

        # Check same type (exception is char var_type with str expr)
        if (expr._type == self._type) or (self._type == ElementType.CHAR and expr._type == ElementType.STRING_PRIMITIVE):
            env.save_variable(self._id, self._type, expr.value, self.line, self.column, False)
            return ExecReturn(value=True, _type=ElementType.BOOL,
                              propagate_method_return=False, propagate_continue=False, propagate_break=False)

        # Error:
        error_msg = f'Asignacion de tipo {expr._type.name} a variable  {self._id} de tipo {self._type.name}'
        global_config.log_semantic_error(error_msg, self.line, self.column)
        raise errors.semantic_error.SemanticError(error_msg, self.line, self.column)

    def ast(self) -> ASTReturn:
        father_ref = global_config.get_unique_number()
        id_ref = global_config.get_unique_number()
        result: str = f'{father_ref}[label="DECLARATION\\n{self._type.name}"]\n' \
                      f'{id_ref}[label={self._id}]\n' \
                      f'{father_ref} -> {id_ref}\n'

        if self.expression is None:
            return ASTReturn(result, father_ref)

        expr_ast = self.expression.ast()
        result += f'{expr_ast.value}\n' \
                  f'{father_ref} -> {expr_ast.head_ref}\n'
        return ASTReturn(result, father_ref)
