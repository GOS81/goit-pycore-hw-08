from handler_command import *
from address_book import *

book = AddressBook()

@input_error
def parse_input(input_command):
    cmd, *args = input_command.split()
    cmd = cmd.lower()

    if cmd == "hello":
        print("Чим я можу вам допомогти?")

    elif cmd == "help":
        print("Введіть одну з команд: hello, add, change, phone, all, exit or close")
    
    elif cmd in ["close", "exit"]:
        print("Ви залишаєте додаток! \nГарного дня!")
        return exit()

    elif cmd == "add":
        add_contact(args, book)

    elif cmd == "change":
        if args[0].capitalize() != None:
            change(args, book)
        else:
            raise ValueError ("Введіть ім'я")
    
    elif cmd == "phone":
        phone(args, book)
    
    elif cmd == "all":
        all(book)

    elif cmd == "add-birthday":
        add_birthday(args, book)

    elif cmd == "show-birthday":
        show_birthday(args, book)

    elif cmd == "birthdays":
        birthdays(book)

    else:
        raise ValueError("Такої команди не знайдено! \nВведіть одну з наступних команд: \nhello, help, add, change, phone, add-birthday, show-birthday, birthdays, all, exit or close")

    return book