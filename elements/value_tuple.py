from elements.element_type import ElementType


class ValueTuple:

    def __init__(self, value, _type: ElementType):
        self._type = _type
        self.value = value

