from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


    def find(self, name):
        for record in self.data.values():
            if record.name.value == name:
                return record

        return None


    def delete(self, name):
        del self.data[name]


    def __str__(self):
        return f'Address Book:\n {'\n '.join(str(record) for record in self.data.values())}'