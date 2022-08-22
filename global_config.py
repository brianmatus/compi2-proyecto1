import secrets
from typing import List, Dict

from errors.lexic_error import LexicError
from errors.semantic_error import SemanticError
from errors.syntactic_error import SyntacticError

from elements.value_tuple import ValueTuple
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


def match_dimensions(supposed: List, arr: List[ValueTuple]) -> bool:

    print("------------------------------------------------------")
    print('supposed')
    print(supposed)
    print("arr")
    print(arr)

    if not isinstance(arr, list):  # Reached end of array
        if len(supposed) is not 0:  # But chain is not completed
            print("False: end of array but not chain")
            return False
        print("True: end of array and chain")
        return True

    else:  # Array is still nested

        if len(supposed) is 0:  # But chain is empty
            print("False:end of chain but not array")
            return False
        # dont you dare return true :P Keep checking more nested levels

    if len(arr) is not supposed[0]:
        print(f'False: supposed-array mismatch: {len(arr)}->{supposed[0]}')
        return False

    index = supposed.pop(0)

    for i in range(index):
        r: bool = match_dimensions(supposed[:], arr[i].value)
        if not r:
            print(f'False:{i}th child returned False')
            return False

    # All children and self returned True
    return True
