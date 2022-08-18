class SyntacticError(Exception):

    def __init__(self, reason: str, line: int, column: int):
        self.reason = reason
        self.row = line
        self.column = column
