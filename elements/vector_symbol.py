from element_types.element_type import ElementType


class VectorSymbol:
    def __init__(self, _id: str, _type: ElementType, content_type: ElementType, deepness: int, value,
                 is_mutable: bool, capacity: int):
        self.value = value
        self._id: str = _id
        self._type: ElementType = _type
        self.is_mutable: bool = is_mutable
        self.deepness: int = deepness
        self.capacity: int = capacity
        self.content_type: ElementType = content_type
