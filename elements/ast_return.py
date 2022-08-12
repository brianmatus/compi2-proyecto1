from elements.env import Environment
from elements.element_type import ElementType


class ASTReturn:
    def __init__(self, value: str, head_ref: int):
        self.value = value
        self.head_ref = head_ref
