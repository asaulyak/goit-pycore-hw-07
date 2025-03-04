from address_book import AddressBook, Record

COMMAND_NAME = 'add'

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            message = f'Failed to add contact: {e}'

            return message, False

    return inner

@input_error
def run(args, context: AddressBook):
    stop = False

    if len(args) < 2:
        raise ValueError("Give me name and phone please.")

    name, phone = args

    if not name or not phone:
        raise ValueError("Give me name and phone please.")

    if not name.isalpha():
        raise ValueError("Invalid name.")

    if not phone.isdigit():
        raise ValueError("Invalid phone number.")

    contact = context.find(name, Record(name))
    contact.add_phone(phone)

    message = "Contact added."

    context.add_record(contact)

    return message, stop
