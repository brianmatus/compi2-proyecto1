import traceback

import analysis.lexer as lexer  # TODO for debug only

from typing import List

import errors.custom_semantic
from returns.parse_result import ParseResult
from analysis.parser import parser

from instructions.instruction import Instruction
from instructions.function_declaration import FunctionDeclaration
from elements.env import Environment

from errors.lexic_error import LexicError
from errors.semantic_error import SemanticError
from errors.syntactic_error import SyntacticError


import global_config



# TODO import: function decl, declaration, array declare, conditional, switch, while, for, logic


def start():  # FIXME this should be replaced with frontend sending the code
    f = open("code.exp", "r")
    input_code: str = f.read()
    f.close()

    result: ParseResult = parse_code(input_code)
    # print("code result:")
    # print(result)


def parse_code(code_string: str) -> ParseResult:
    # Debug tokenizer
    # lexer.lexer.input(code_string)
    # # Tokenize
    # while True:
    #     tok = lexer.lexer.token()
    #     if not tok:
    #         return
    #     print(tok)

    code_string += "\n"
    global_config.main_environment = Environment(None)

    lexic_error_list = []
    syntactic_error_list = []
    semantic_error_list = []
    # func list
    global_config.console_output = ""
    try:
        instruction_set = parser.parse(code_string)

    except errors.custom_semantic.CustomSemanticError as err:
        traceback.print_exc()
        print(err)
        print("Unhandled semantic error?, custom semantic?")
        # already logged, do nothing

        main_environment = Environment(None)
        return ParseResult(lexic_error_list, syntactic_error_list, semantic_error_list,
                           ast_tree='digraph G {\na[label="PARSE ERROR :( (semantic)"]\n}',
                           console_output=global_config.console_output, symbol_table=[])

    except Exception as err:
        print("Unhandled (lexic?)/semantic error?")
        traceback.print_exc()
        print(err)

        # TODO implement semantic differentiation for missing token / unexpected one (in case i missed one)

        main_environment = Environment(None)
        return ParseResult(lexic_error_list, syntactic_error_list, semantic_error_list,
                           ast_tree='digraph G {\na[label="PARSE ERROR :( (syntactic)"]\n}',
                           console_output=global_config.console_output, symbol_table=[])

    print("#############################################################################")
    print("#############################################################################")
    print("#############################################################################")
    print("#############################################################################")


    print(instruction_set)

    # Register all functions and modules
    try:
        instruction: Instruction
        for instruction in instruction_set:

            if not isinstance(instruction, FunctionDeclaration):  # Or Module declaration
                error_msg = f"No se permiten declaraciones globales."
                global_config.log_semantic_error(error_msg, instruction.line, instruction.column)
                raise SemanticError(error_msg, instruction.line, instruction.column)

            print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            instruction.execute(global_config.main_environment)

        main_func: FunctionDeclaration = global_config.function_list.get("main")
        if main_func is None:
            error_msg = f"No se definió una función main"
            global_config.log_semantic_error(error_msg, -1, -1)
            raise SemanticError(error_msg, -1, -1)

        print(main_func.params)
        if main_func.params[0] is not None:
            error_msg = f"ADVERTENCIA: La función main debe llamarse sin argumentos. Estos serán ignorados"
            global_config.log_semantic_error(error_msg, -1, -1)
            # No need to raise, they will only get ignored
            # raise SemanticError(error_msg, -1, -1)

        # "Abandonen la esperanza todos los que entren aquí"
        for instruction in main_func.instructions:
            instruction.execute(main_func.environment)







        # print("Resulting AST:")
        # print(generate_ast_tree(instruction_set))
        print("Resulting environment:")
        _symbol_table = main_func.environment.symbol_table  # TODO delete me, debug only
        _function_list = global_config.function_list
        print(global_config.main_environment)
        print("Resulting function list:")
        # print(function_list)
        print("Resulting symbol table:")
        print(generate_symbol_table(instruction_set, "Main"))
        print("Resulting console output:")
        print(global_config.console_output)

    except Exception as err:
        traceback.print_exc()
        print(err)

        print("#####################Errores Lexicos:###################")
        lexic: LexicError
        for lexic in lexic_error_list:
            print("[row:%s,column:%s]Error Lexico: <%s> no reconocido", lexic.row, lexic.column, lexic.reason)

        print("#####################Errores Sintactico:###################")
        syntactic: SyntacticError
        for syntactic in syntactic_error_list:
            print("[row:%s,column:%s]ERROR:%s", syntactic.row, syntactic.column, syntactic.reason)

        print("#####################Errores Semantico:###################")
        semantic: SemanticError
        for semantic in semantic_error_list:
            print("[row:%s,column:%s]ERROR:%s", semantic.row, semantic.column, semantic.reason)

        global_config.main_environment = Environment(None)
        return ParseResult(lexic_error_list, syntactic_error_list, semantic_error_list,
                           ast_tree=generate_ast_tree(instruction_set),
                           console_output=global_config.console_output,
                           symbol_table=generate_symbol_table(instruction_set, "Main"))


def generate_symbol_table(instruction_set: List[Instruction], env_name: str) -> List[List[str]]:
    pass  # TODO implement


def generate_ast_tree(instruction_set: List[Instruction]) -> str:
    return ""  # TODO this project doesn't require it
    # instructions_father_ref = global_config.get_unique_number()
    # ast_tree: str = f'digraph{{\n{instructions_father_ref}[label="Instructions"]\n'
    #
    # instructions_ast: str = generate_instruction_set_ast(instruction_set, instructions_father_ref)
    #
    # ast_tree += f'{instructions_ast}\n}}'
    # return ast_tree


def generate_instruction_set_ast(instruction_set: List[Instruction], father_ref: int) -> str :
    _str = ''
    instruction: Instruction
    for instruction in instruction_set:
        instruction_ast = instruction.ast()
        _str += f'{instruction_ast.value}\n' \
                f'{father_ref} -> {instruction_ast.head_ref}\n'

    return _str

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
