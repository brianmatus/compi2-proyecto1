import ply.yacc as yacc

from elements.element_type import ElementType

from instructions.declaration import Declaration

from expressions.literal import Literal
from elements.arithmetic_type import ArithmeticType
from expressions.arithmetic import Arithmetic


from analysis.lexer import tokens

precedence = (
    ('left', 'SUB', 'SUM'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)


def p_matus(p):
    """matus : instructions"""
    p[0] = p[1]


def p_instructions_rec(p):
    """instructions : instructions instruction"""
    p[0] = p[1].append(p[2])


def p_instructions(p):
    """instructions : instruction"""
    p[0] = [p[1]]


def p_instruction(p):
    """instruction : var_declaration"""  # since all here are p[0] = p[1] (except void_inst) add all productions here
    p[0] = p[1]


def p_var_declaration_1(p):
    """var_declaration : LET MUTABLE ID COLON variable_type EQUAL expression SEMICOLON"""
    p[0] = Declaration(p[3], p[5], p[7], p.lineno(1), -1)


#######################################################################################################################
def p_variable_type_i64(p):
    """variable_type : TYPE_I64"""
    p[0] = ElementType.INT


def p_variable_type_f64(p):
    """variable_type : TYPE_F64"""
    p[0] = ElementType.FLOAT


def p_variable_type_bool(p):
    """variable_type : TYPE_BOOL"""
    p[0] = ElementType.BOOL


def p_variable_type_char(p):
    """variable_type : TYPE_CHAR"""
    p[0] = ElementType.CHAR


def p_variable_type_amper_str(p):
    """variable_type : TYPE_AMPER_STR"""
    p[0] = ElementType.STRING_PRIMITIVE


def p_variable_type_string(p):
    """variable_type : TYPE_STRING"""
    p[0] = ElementType.STRING_CLASS
#######################################################################################################################


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################


def p_expression_plus(p):
    """expression : expression SUM expression"""
    p[0] = Arithmetic(p[1], p[3], ArithmeticType.SUM, p.lineno(1), -1)


def p_expression_minus(p):
    """expression : expression SUB expression"""
    p[0] = Arithmetic(p[1], p[3], ArithmeticType.SUB, p.lineno(1), -1)


def p_expression_mult(p):
    """expression : expression MULT expression"""
    p[0] = Arithmetic(p[1], p[3], ArithmeticType.MULT, p.lineno(1), -1)


def p_expression_div(p):
    """expression : expression DIV expression"""
    p[0] = Arithmetic(p[1], p[3], ArithmeticType.DIV, p.lineno(1), -1)


def p_expression_mod(p):
    """expression : expression MOD expression"""
    p[0] = Arithmetic(p[1], p[3], ArithmeticType.MOD, p.lineno(1), -1)


def p_expression_uminus(p):
    """expression : SUB expression %prec UMINUS"""
    p[0] = Arithmetic(p[2], p[2], ArithmeticType.NEG, p.lineno(1), -1)


def p_expression_parenthesis(p):
    """expression : PARENTH_O expression PARENTH_C"""
    p[0] = p[2]


def p_expression_integer(p):
    """expression : INTEGER"""
    p[0] = Literal(p[1], ElementType.INT, p.lineno(1), -1)
    # print(p.lexpos(1))


def p_expression_float(p):
    """expression : FLOAT"""
    p[0] = Literal(p[1], ElementType.FLOAT, p.lineno(1), -1)


def p_error(p):
    print("syntactic error")
    print(p)


parser = yacc.yacc()  # los increibles
