from address_book import AddressBook

COMMAND_NAME = 'add-birthday'

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            message = f'Failed to add contact\'s birthday: {e}'

            return message, False
        except IndexError as e:
            message = f'Invalid contact: {e}'

            return message, False

    return inner

@input_error
def run(args, context: AddressBook):
    stop = False

    if len(args) < 2:
        raise ValueError("Give me name and birthday please.")

    name, birthday = args

    if not name or not birthday:
        raise ValueError("Give me name and birthday please.")

    if not name.isalpha():
        raise ValueError("Invalid name.")

    contact = context.find(name)

    if not contact:
        raise IndexError("Contact not found.")

    contact.add_birthday(birthday)

    message = "Birthday added."

    return message, stop
