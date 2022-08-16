import secrets
from typing import List, Dict

from errors.lexic_error import LexicError
from errors.semantic_error import SemanticError
from errors.syntactic_error import SyntacticError


lexic_error_list: List[LexicError] = []
syntactic_error_list: List[SyntacticError] = []
semantic_error_list: List[SemanticError] = []


ALLOW_NESTED_VARIABLE_OVERRIDE = True
unique_counter = 0
console_output: str = ""
# TODO function_list = Dict[func_name:str, func:func_decl]


def log_to_console(txt: str):
    global console_output
    console_output += txt


def log_lexic_error(foreign: str, row: int, column: int):
    global console_output
    lexic_error_list.append(LexicError(f'Signo <{foreign}> no reconocido', row, column))
    print(f'Logged Lexic Error:{row}-{column} -> Signo <{foreign}> no reconocido')
    console_output += f'[row:{row},column:{column}]Error Lexico: <{foreign} no reconocido\n'


def log_syntactic_error(reason: str, row: int, column: int):
    global console_output
    syntactic_error_list.append(SyntacticError(reason, row, column))
    print(f'Logged Syntactic Error:{row}-{column} -> {reason}')
    console_output += f'[row:{row},column:{column}]Error Sintáctico:{reason} \n'


def log_semantic_error(reason: str, row: int, column: int):
    global console_output
    semantic_error_list.append(SemanticError(reason, row, column))
    print(f'Logged Semantic Error:{row}-{column} -> {reason}')
    console_output += f'[row:{row},column:{column}]Error Semántico:{reason}\n'


def get_unique_number() -> int:
    global unique_counter
    unique_counter += 1
    return unique_counter


def random_hex_color_code() -> str:
    return "#" + secrets.token_hex(2)

