import analysis.parser as parser

ALLOW_NESTED_VARIABLE_OVERRIDE = True
unique_counter = 0


def start():
    f = open("code.exp", "r")
    input_code: str = f.read()
    f.close()

    result: str = parser.parser.parse(input_code)
    print("code result:")
    print(result)


def get_unique_number() -> int:
    global unique_counter
    unique_counter += 1
    return unique_counter











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
