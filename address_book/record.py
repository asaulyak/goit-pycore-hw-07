from .name import Name
from .phone import Phone


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def edit_phone(self, phone_number, new_phone):
        for p in self.phones:
            if p.value == phone_number:
                p.update(new_phone)

                return

        raise ValueError(f"Phone number {phone_number} not found")

    def find_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:

                return p

    def remove_phone(self, phone_number):
        for p in self.phones:
            if p.value == phone_number:
                self.phones.remove(p)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
