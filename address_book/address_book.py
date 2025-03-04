from collections import UserDict
from .record import Record


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name, default = None) -> Record:
        return self.data.get(name, default)


    def delete(self, name):
        del self.data[name]


    def __str__(self):
        return f'Address Book:\n {'\n '.join(str(record) for record in self.data.values())}'