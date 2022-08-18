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

    def __init__(self, _id: str, _type: ElementType, expression: Expression, is_mutable: bool, line: int, column: int):
        super().__init__(line, column)
        self._id = _id
        self._type: ElementType = _type
        self.expression: Expression = expression
        self.is_mutable = is_mutable

        if self._type is None:
            print(f'Instance of declaration with id:{self._id} type:inferred')
        else:
            print(f'Instance of declaration with id:{self._id} type:{self._type.name}')

    def execute(self, env: Environment) -> ExecReturn:
        expr: ValueTuple

        # Declaration without assignment, using default values  (not possible? idk
        # if self.expression is None:
        #     match self._type:
        #         case ElementType.INT:
        #             env.save_variable(self._id, self._type, 0, self.line, self.column, False)
        #         case ElementType.FLOAT:
        #             env.save_variable(self._id, self._type, float(0.0), self.line, self.column, False)
        #         case ElementType.BOOL:
        #             env.save_variable(self._id, self._type, False, self.line, self.column, False)

        # Using not_init instead
        if self.expression is None:
            env.save_variable(self._id, self._type, None,
                              is_mutable=self.is_mutable, is_init=False, is_array=False,
                              line=self.line, column=self.column,)

            return ExecReturn(ElementType.BOOL, True, False, False, False)

        expr: ValueTuple = self.expression.execute(env)

        # Infer if not explicitly specified
        if self._type is None:
            self._type = expr._type

        # Check same type (exception is char var_type with str expr_type)
        if (expr._type == self._type) or\
                (self._type == ElementType.CHAR and expr._type == ElementType.STRING_PRIMITIVE):

            env.save_variable(self._id, self._type, expr.value,
                              is_mutable=self.is_mutable, is_init=True, is_array=False,
                              line=self.line, column=self.column, )

            return ExecReturn(self._type, True, False, False, False)

        # Error:
        error_msg = f'Asignacion de tipo {expr._type.name} a variable  {self._id} de tipo {self._type.name}'
        global_config.log_semantic_error(error_msg, self.line, self.column)
        raise errors.semantic_error.SemanticError(error_msg, self.line, self.column)

    def ast(self) -> ASTReturn:
        father_ref = global_config.get_unique_number()
        id_ref = global_config.get_unique_number()
        the_type: str
        if self._type is None:
            the_type = "Inferred"
        else:
            the_type = self._type.name

        result: str = f'{father_ref}[label="DECLARATION\\n{the_type}"]\n' \
                      f'{id_ref}[label={self._id}]\n' \
                      f'{father_ref} -> {id_ref}\n'

        if self.expression is None:
            return ASTReturn(result, father_ref)

        expr_ast = self.expression.ast()
        result += f'{expr_ast.value}\n' \
                  f'{father_ref} -> {expr_ast.head_ref}\n'
        return ASTReturn(result, father_ref)
