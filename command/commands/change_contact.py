from address_book import AddressBook

COMMAND_NAME = 'change'

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as e:
            message = f'Invalid contact: {e}'

            return message, False
        except ValueError as e:
            message = f'Failed to update contact: {e}'

            return message, False

    return inner

@input_error
def run(args, context: AddressBook):
    stop = False

    if len(args) < 3:
        raise ValueError("Give me name, old phone and new phone please.")

    name, old_phone, phone = args

    if not name or not phone or not old_phone:
        raise ValueError("Give me name, old phone and new phone please.")

    contact = context.find(name)

    if not contact:
        raise IndexError("Contact not found.")

    contact.edit_phone(old_phone, phone)

    message = "Contact updated."

    return message, stop