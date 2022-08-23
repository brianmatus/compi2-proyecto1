import ply.lex as lex

reserved = {
    'fn': 'FUNCTION',
    'let': 'LET',
    'mut': 'MUTABLE',
    'i64': 'TYPE_I64',
    'f64': 'TYPE_F64',
    'bool': 'TYPE_BOOL',
    'true': 'BOOL_TRUE',
    'false': 'BOOL_FALSE',
    'char': 'TYPE_CHAR',
    'str': 'TYPE_AMPER_STR',
    'String': 'TYPE_STRING',
    'println': 'PRINTLN'
}

tokens = [
    'COMMENT',
    'SUM',
    'SUB',
    'MULT',
    'DIV',
    'MOD',
    'OPE_EQUAL',
    'OPE_NEQUAL',
    'OPE_LESS',
    'OPE_LESS_EQUAL',
    'OPE_MORE',
    'OPE_MORE_EQUAL',
    'LOGIC_OR',
    'LOGIC_AND',
    'LOGIC_NOT',
    'INTEGER',
    'FLOAT',
    'STRING_TEXT',
    'CHAR',
    'ID',
    'AMPERSAND',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'EQUAL',
    'PARENTH_O',
    'PARENTH_C',
    'BRACKET_O',
    'BRACKET_C',
] + list(reserved.values())


t_ignore = '\t '

def t_COMMENT(t):
    r"""//[^\n]*\n"""
    pass



t_SUM = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'/(?!/)'
t_MOD = r'\%'


t_OPE_EQUAL = r'=='
t_OPE_NEQUAL = r'!='
t_OPE_LESS_EQUAL = r'<='
t_OPE_MORE_EQUAL = r'>='
t_OPE_LESS = r'<'
t_OPE_MORE = r'>'

t_LOGIC_AND = r'&&'
t_LOGIC_OR = r'\|\|'
t_LOGIC_NOT = r'!'

t_PARENTH_O = r'\('
t_PARENTH_C = r'\)'
t_BRACKET_O = r'\['
t_BRACKET_C = r'\]'


t_SEMICOLON = r';'
t_COLON = r':'
t_COMMA = r','
t_AMPERSAND = r'&'

t_EQUAL = r'='


def t_ID(t):
    r"""[a-zA-Z_][a-zA-Z_0-9]*"""
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t


def t_STRING_TEXT(t):
    # TODO transform special characters
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t


def t_CHAR(t):
    # TODO check only one char appearing (special chars?)
    r"""'[^']*'"""
    t.value = t.value[1:-1]
    return t


def t_FLOAT(t):
    r"""\d+\.\d+"""
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value out of bounds %d", t.value)
        t.value = 0
    return t


def t_INTEGER(t):
    r"""\d+"""
    t.value = int(t.value)
    return t




def t_newline(t):
    r"""\n+"""
    t.lexer.lineno += t.value.count('\n')


def t_eof(t):
    return None

def t_error(t):
    print(f'LEX: Illegal character {t.value[0]!r} line:{t.lexer.lineno} column:{find_column(t)}')
    t.lexer.skip(1)


def find_column(token):
    line_start = lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()









