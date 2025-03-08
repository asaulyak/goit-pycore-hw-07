from address_book import AddressBook

COMMAND_NAME = 'birthdays'


def run(_, context: AddressBook):
    stop = False

    message = context.get_upcoming_birthdays()

    return message, stop