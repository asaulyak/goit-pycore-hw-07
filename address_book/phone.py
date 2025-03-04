from .field import Field

class Phone(Field):
    def __init__(self, value):
        if not self.__validate(value):
            raise ValueError('Invalid phone number')

        super().__init__(value)

    def __validate(self, value):
        return len(value) == 10 and value.isdigit()

