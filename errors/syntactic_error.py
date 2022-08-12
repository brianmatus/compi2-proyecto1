class SyntacticError:

    def __init__(self, reason: str, row: int, column: int):
        self.reason = reason
        self.row = row
        self.column = column
