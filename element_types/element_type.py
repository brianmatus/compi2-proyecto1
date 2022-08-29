from enum import Enum

ElementType = Enum('ElementType',
              ' '.join([
                  'INT',
                  'USIZE',
                  'FLOAT',
                  'BOOL',
                  'CHAR',
                  'STRING_PRIMITIVE',  # literal
                  'STRING_CLASS',  # class (using .to_owned() or .to_string()
                  'ARRAY_EXPRESSION',  # only used internally
                  'VOID',
                  'EQUAL',
                  'OPE_EQUAL',
                  'OPE_NEQUAL',
                  'OPE_LESS',
                  'OPE_LESS_EQUAL',
                  'OPE_MORE',
                  'OPE_MORE_EQUAL',
                  'LOGIC_OR',
                  'LOGIC_AND',
                  'LOGIC_NOT',
                  'TERNARY',
                  'GROUP_PAREN_O',
                  'GROUP_PAREN_C',
                  'GROUP_KEY_O',
                  'GROUP_KEY_C',
                  'BRACKET_O',
                  'BRACKET_C',
                  'SEMI_COLON',
                  'COLON',
                  # Reserved
                  'TYPE_INT',
                  'TYPE_USIZE',
                  'TYPE_FLOAT',
                  'TYPE_CHAR',
                  'TYPE_STRING_PRIMITIVE',
                  'TYPE_STRING_CLASS',
                  'STATEMENT_IF',
                  'STATEMENT_ELSE',
                  'STATEMENT_MATCH',
                  'STATEMENT_CASE',
                  'ITERATIVE_BREAK',
                  'ITERATIVE_CONTINUE',
                  'ITERATIVE_WHILE',
                  'ITERATIVE_FOR',
                  'ITERATIVE_DO'
              ]))
