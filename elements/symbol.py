from elements.element_type import ElementType


class Symbol:
    def __init__(self, value, _id: str, _type: ElementType, is_array: bool):
        self.value = value
        self._id = _id
        self._type = _type
        self.is_array = is_array
