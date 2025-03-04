from command import parser
from address_book import AddressBook

def main():
    contacts = AddressBook()

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        cmd, *args = parser.parse_command(user_input)

        command = parser.get_command(cmd)

        message, stop = command(args, contacts)

        print(message)

        if stop:
            break


if __name__ == "__main__":
    main()