
class ArrayDefType:

    def __init__(self, is_nested_array: bool, content):  # Content should only be ElementType or ArrayDefType
        self.is_nested_array = is_nested_array
        self.content = content
