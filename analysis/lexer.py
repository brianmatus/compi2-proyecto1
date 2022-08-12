import ply.lex as lex

reserved = {
    'fn': 'FUNCTION',
    'mut': 'MUTABLE',
    'i64': 'I64',
}

tokens = [
    'SUM',
    'SUB',
    'MULT',
    'DIV',
    'INTEGER',
    'FLOAT',
    'STRING', # here TODO be careful with string primitive and string class
    'ID',
    'SEMICOLON',
    'COLON',
    'COMMA',
    'PARENTH_O',
    'PARENTH_C',
    'BRACKET_O',
    'BRACKET_C',
] + list(reserved.values())


t_ignore = '[\t ]'

t_SUM = r'\+'
t_SUB = r'\-'
t_MULT = r'\*'
t_DIV = r'/'
t_PARENTH_O = r'\('
t_PARENTH_C = r'\)'


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


def t_error(t):
    print(f'LEX: Illegal character {t.value[0]!r} line:{t.lexer.lineno} column:{find_column(t)}')
    t.lexer.skip(1)


def find_column(token):
    line_start = lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


lexer = lex.lex()









