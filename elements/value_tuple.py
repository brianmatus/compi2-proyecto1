from element_types.element_type import ElementType


class ValueTuple:

    def __init__(self, value, _type: ElementType):
        self._type = _type
        self.value = value

    def __str__(self):
        return f'ValTup(v:{self.value}, t:{self._type})'

    def __repr__(self):
        return f'ValTup(v:{self.value}, t:{self._type})'

