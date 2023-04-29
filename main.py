def input_error(handler):
    def inner(name, *args):
        try:
            return handler(name, *args)
        except (KeyError, ValueError, IndexError) as error:
            return str(error)
    return inner


@input_error
def add_contact(contacts, name, phone):
    contacts[name.lower()] = phone
    return f"Contact {name} added."


@input_error
def change_contact(contacts, name, phone):
    if name.lower() in contacts:
        contacts[name.lower()] = phone
        return f"Contact {name} updated."
    else:
        raise KeyError("Contact not found.")


@input_error
def find_contact(contacts, name):
    return contacts[name.lower()]


@input_error
def show_all(contacts):
    result = ["Contacts:"]
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant!")

    while True:
        user_input = input("\nEnter your command: ").strip().lower()
        words = user_input.split()

        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print("How can I help you?")
        elif words[0] == "add":
            print(add_contact(contacts, words[1], words[2]))
        elif words[0] == "change":
            print(change_contact(contacts, words[1], words[2]))
        elif words[0] == "phone":
            try:
                print(find_contact(contacts, words[1]))
            except KeyError:
                print("Contact not found.")
        elif user_input == "show all":
            print(show_all(contacts))
        else:
            print("Command not recognized. Try again.")


if __name__ == "__main__":
    main()
