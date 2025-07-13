from parse_input import parse_input

def main():
    print("\nВітаємо в телефонному довіднику!")
    while True:
        user_command = input("Введіть команду >>> ").strip()
        parse_input(user_command)

if __name__ == "__main__":
    main()