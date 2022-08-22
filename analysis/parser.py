import ply.yacc as yacc
import analysis.lexer as lexer

from element_types.element_type import ElementType

from instructions.declaration import Declaration
from instructions.array_declaration import ArrayDeclaration
from element_types.array_def_type import ArrayDefType
from expressions.array_expression import ArrayExpression


from expressions.literal import Literal
from element_types.arithmetic_type import ArithmeticType
from expressions.arithmetic import Arithmetic
from element_types.logic_type import LogicType
from expressions.logic import Logic

tokens = lexer.tokens


start = 'marian'

# start = 'array_type'

precedence = (

    ('left', 'LOGIC_OR'),
    ('left', 'LOGIC_AND'),
    # needs parenthesis according to rust
    ('nonassoc', 'OPE_EQUAL', 'OPE_NEQUAL', 'OPE_LESS', 'OPE_MORE', 'OPE_LESS_EQUAL', 'OPE_MORE_EQUAL'),
    ('left', 'SUB', 'SUM'),
    ('left', 'MULT', 'DIV', 'MOD'),
    ('nonassoc', 'UMINUS', "LOGIC_NOT"),  # nonassoc according to rust, i think 'right'

)


def p_marian(p):  # M&B ♥
    """marian : instructions"""
    p[0] = p[1]


def p_instructions_rec(p):
    """instructions : instructions instruction"""
    p[0] = p[1] + [p[2]]


def p_instructions(p):
    """instructions : instruction"""
    p[0] = [p[1]]


def p_instruction(p):   # since all here are p[0] = p[1] (except void_inst) add all productions here
    """instruction : var_declaration
    | array_declaration"""
    p[0] = p[1]


#############################################SIMPLE VARIABLE DECLARATION ###############################################
def p_var_declaration_1(p):
    """var_declaration : LET MUTABLE ID COLON variable_type EQUAL expression SEMICOLON"""
    p[0] = Declaration(p[3], p[5], p[7], True, p.lineno(1), -1)


def p_var_declaration_2(p):
    """var_declaration : LET MUTABLE ID EQUAL expression SEMICOLON"""
    p[0] = Declaration(p[3], None, p[5], True, p.lineno(1), -1)


def p_var_declaration_3(p):
    """var_declaration : LET ID COLON variable_type EQUAL expression SEMICOLON"""
    p[0] = Declaration(p[2], p[4], p[6], False, p.lineno(1), -1)


def p_var_declaration_4(p):
    """var_declaration : LET ID EQUAL expression SEMICOLON"""
    p[0] = Declaration(p[2], None, p[4], False, p.lineno(1), -1)


#############################################ARRAY VARIABLE DECLARATION ###############################################
def p_array_declaration_1(p):    # array_expression instead of expression
    """array_declaration : LET MUTABLE ID COLON array_type EQUAL array_expression SEMICOLON"""
    p[0] = ArrayDeclaration(p[3], p[5], p[7], True, p.lineno(1), -1)
    print("p_array_declaration_1")


def p_array_declaration_2(p):
    """array_declaration : LET MUTABLE ID COLON array_type SEMICOLON"""
    p[0] = ArrayDeclaration(p[3], p[5], None, True, p.lineno(1), -1)


def p_array_declaration_3(p):
    """array_declaration : LET ID COLON array_type EQUAL array_expression SEMICOLON"""
    p[0] = ArrayDeclaration(p[2], p[4], p[6], False, p.lineno(1), -1)


def p_array_declaration_4(p):
    """array_declaration : LET ID COLON array_type SEMICOLON"""
    p[0] = ArrayDeclaration(p[2], p[4], None, False, p.lineno(1), -1)


#####################################################

def p_array_type_r(p):
    """array_type : BRACKET_O array_type SEMICOLON expression BRACKET_C"""
    p[0] = ArrayDefType(True, p[2], p[4])
    print("p_array_type_r")


def p_array_type(p):
    """array_type : BRACKET_O variable_type SEMICOLON expression BRACKET_C"""
    p[0] = ArrayDefType(False, p[2], p[4])
    print("p_array_type")


########################################

def p_array_expression_list(p):
    """array_expression : BRACKET_O expression_list BRACKET_C"""
    p[0] = ArrayExpression(p[2], False, None, p.lineno(1), -1)
    print("p_array_expression_list")


def p_array_expression_expansion(p):
    """array_expression : BRACKET_O expression SEMICOLON expression BRACKET_C"""
    p[0] = ArrayExpression(p[2], True, p[4], p.lineno(1), -1)
    print("p_array_expression_expansion")


def p_expression_list_r(p):
    """expression_list : expression_list COMMA expression
    | expression_list COMMA array_expression"""
    p[1].append(p[3])
    p[0] = p[1]
    print("p_expression_list_r")


def p_expression_list(p):
    """expression_list : expression
    | array_expression"""
    p[0] = [p[1]]
    print("p_expression_list")

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
    """variable_type : AMPERSAND TYPE_AMPER_STR"""
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


def p_expression_integer(p):
    """expression : INTEGER"""
    p[0] = Literal(p[1], ElementType.INT, p.lineno(1), -1)
    # print(p.lexpos(1))


def p_expression_float(p):
    """expression : FLOAT"""
    p[0] = Literal(p[1], ElementType.FLOAT, p.lineno(1), -1)


def p_expression_string(p):
    """expression : STRING_TEXT"""
    p[0] = Literal(p[1], ElementType.STRING_PRIMITIVE, p.lineno(1), -1)


def p_expression_char(p):
    """expression : CHAR"""
    p[0] = Literal(p[1], ElementType.CHAR, p.lineno(1), -1)


def p_expression_true(p):
    """expression : BOOL_TRUE"""
    p[0] = Literal(True, ElementType.BOOL, p.lineno(1), -1)


def p_expression_false(p):
    """expression : BOOL_FALSE"""
    p[0] = Literal(False, ElementType.BOOL, p.lineno(1), -1)


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


# RELATIONAL

def p_expression_ope_equal(p):
    """expression : expression OPE_EQUAL expression"""
    p[0] = Logic(p[1], p[3], LogicType.OPE_EQUAL, p.lineno(1), -1)


def p_expression_ope_nequal(p):
    """expression : expression OPE_NEQUAL expression"""
    p[0] = Logic(p[1], p[3], LogicType.OPE_NEQUAL, p.lineno(1), -1)


def p_expression_ope_less(p):
    """expression : expression OPE_LESS expression"""
    p[0] = Logic(p[1], p[3], LogicType.OPE_LESS, p.lineno(1), -1)


def p_expression_ope_less_equal(p):
    """expression : expression OPE_LESS_EQUAL expression"""
    p[0] = Logic(p[1], p[3], LogicType.OPE_LESS_EQUAL, p.lineno(1), -1)


def p_expression_ope_more(p):
    """expression : expression OPE_MORE expression"""
    p[0] = Logic(p[1], p[3], LogicType.OPE_MORE, p.lineno(1), -1)


def p_expression_ope_more_equal(p):
    """expression : expression OPE_MORE_EQUAL expression"""
    p[0] = Logic(p[1], p[3], LogicType.OPE_MORE_EQUAL, p.lineno(1), -1)


# LOGICAL
def p_expression_logic_or(p):
    """expression : expression LOGIC_OR expression"""
    p[0] = Logic(p[1], p[3], LogicType.LOGIC_OR, p.lineno(1), -1)


def p_expression_logic_and(p):
    """expression : expression LOGIC_AND expression"""
    p[0] = Logic(p[1], p[3], LogicType.LOGIC_AND, p.lineno(1), -1)


def p_expression_logic_not(p):
    """expression : LOGIC_NOT expression"""
    p[0] = Logic(p[2], p[2], LogicType.LOGIC_NOT, p.lineno(1), -1)


def p_error(p):
    print("Syntax error::Unexpected token")
    print(p)

    print(f"next token is {parser.token()}")
    print(f"2nd next token is {parser.token()}")


parser = yacc.yacc()  # los increibles

#
#                                        (                          )
#                                         \                        /
#                                        ,' ,__,___,__,-._         )
#                                        )-' ,    ,  , , (        /
#                                        ;'"-^-.,-''"""\' \       )
#                                       (      (        ) /  __  /
#                                        \o,----.  o  _,'( ,.^. \
#                                        ,'`.__  `---'    `\ \ \ \_
#                                 ,.,. ,'                   \    ' )
#                                 \ \ \\__  ,------------.  /     /
# UN COMPILADOR NO TERMINADO     ( \ \ \( `---.-`-^--,-,--\:     :
#                                 \       (   (""""""`----'|     :
#                                  \   `.  \   `.          |      \
#                                   \   ;  ;     )      __ _\      \
#                                   /     /    ,-.,-.'"Y  Y  \      `.
#                                  /     :    ,`-'`-'`-'`-'`-'\       `.
#                                 /      ;  ,'  /              \        `
#                                /      / ,'   /                \

