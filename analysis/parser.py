import ply.yacc as yacc

from expressions.literal import Literal
from elements.element_type import ElementType


from analysis.lexer import tokens

precedence = (
    ('left', 'SUB', 'SUM'),
    ('left', 'MULT', 'DIV'),
    ('right', 'UMINUS'),
)


def p_matus(p):
    """matus : expression"""
    p[0] = p[1]


def p_expression_plus(p):
    """expression : expression SUM expression"""
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    """expression : expression SUB expression"""
    p[0] = p[1] - p[3]


def p_expression_mult(p):
    """expression : expression MULT expression"""
    p[0] = p[1] * p[3]


def p_expression_div(p):
    """expression : expression DIV expression"""
    p[0] = p[1] / p[3]


def p_expression_uminus(p):
    """expression : SUB expression %prec UMINUS"""
    p[0] = 0 - p[2]


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
