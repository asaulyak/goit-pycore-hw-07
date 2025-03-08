from address_book import AddressBook

COMMAND_NAME = 'all'

def run(_, context: AddressBook):

    message = str(context)
    stop = False

    return message, stop