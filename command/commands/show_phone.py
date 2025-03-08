from address_book import AddressBook

COMMAND_NAME = 'phone'

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError as e:
            message = f'Invalid contact: {e}'

            return message, False
        except KeyError as e:
            message = f'Invalid phone: {e}'

            return message, False
        except ValueError as e:
            message = f'Failed to get contact: {e}'

            return message, False

    return inner

@input_error
def run(args, context: AddressBook):
    if len(args) < 1:
        raise ValueError("Give me contact name please.")

    name = args[0]
    stop = False

    if not name:
        raise IndexError("Provide contact name please.")

    contact = context.find(name)

    if not contact:
        raise IndexError("Contact not found.")

    message = '; '.join(str(phone) for phone in contact.phones)

    return message, stop