class Attribute:

    """define the attributes of a class
    >>> a = Attribute('first_attribute', 'string')
    >>> print(a.name)
    first_attribute
    >>> print(a.type)
    str
    """

    def __init__(self, new_name, new_type):
        self.name = new_name.replace(" ", "")
        self.type = self.find_type(new_type)

    def __str__(self):
        # Jin
        # This is how you declare the type of a variable type in Python 3.6
        # age: int = 1  OR
        # age: int
        return f"        self.{self.name}: {self.type}\n"
        # return f"        self.{self.name} -> {self.type} =  # ToDo\n"

    def find_type(self, new_type):
        if "string" in new_type:
            return "str"
        elif "number" in new_type:
            return "int"
        elif "list" in new_type:
            return "list"
        elif "tuple" in new_type:
            return "tuple"
        else:
            return ""

    # Jin
    @staticmethod
    def find_type(new_type):
        if "string" in new_type:
            return "str"
        elif "number" in new_type:
            return "int"
        elif "list" in new_type:
            return "list"
        elif "tuple" in new_type:
            return "tuple"
        else:
            return ""


if __name__ == "__main__":
    from doctest import testmod
    testmod()
