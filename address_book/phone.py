from .field import Field

class Phone(Field):
    def __init__(self, value):
        self._validate(value)

        super().__init__(value)

    def _validate(self, value):
        valid = len(value) == 10 and value.isdigit()

        if not valid:
            raise ValueError('Invalid phone number')


    def __str__(self):
        return f'({self.value[:3]}) {self.value[3:6]}-{self.value[6:]}'