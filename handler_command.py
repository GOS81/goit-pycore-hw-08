
from functools import wraps
from address_book import *
import pickle

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Упс, сталась помилка: {e}")
    return inner

@input_error
def add_contact(args, book):
    if len(args) >= 2:
        name, phone, *_ = args
        record = book.find(name.lower())
        if record is None:
            record = Record(name.lower())
            book.add_record(record)
            print(f"Контакт {name.capitalize()} створено!")
        if phone:
            record.add_phone(phone)
        print(f"Номер телефону {phone} додано до контакта {name.capitalize()}")
    else:
        raise ValueError ("Введіть ім'я і номер телефону")

@input_error
def change(args, book):
    if len(args) >= 3:
        name, phone_old, phone_new, *_ = args
        name_find = book.find(name.lower())
        if name_find != None:
            name_find.edit_phone(phone_old, phone_new)
            print(f"Номер телефона контакта {name.capitalize()} змінено на {phone_new}")
        else:
            raise KeyError ("Контакт не знайдено")
    else:
        raise ValueError ("Введіть всі необхідні данні: ім'я, старий і новий номери телефону")

@input_error
def phone(args, book):
    if len(args) >= 1:
        name, *_ = args
        name_find = book.find(name.lower())
        if name_find != None:
            print(name_find)
        else:
            KeyError ("Контакт не знайдено")
    else:
        raise ValueError ("Введіть ім'я")

@input_error
def all(book):
    for name, record in book.data.items():
        print(record)

@input_error
def add_birthday(args, book):
    if len(args) >= 2:
        name, birthday, *_ = args
        name_find = book.find(name.lower())
        if name_find !=None:
            name_find.add_birthday(birthday)
            print(f"До контакта {name.capitalize()} додано день народження {birthday}")
        else:
            raise KeyError ("Контакт не знайдено. Спробуйте інше ім'я")
    else:
        raise ValueError ("Введіть всі необхідні данні: ім'я, дату народження")

@input_error
def show_birthday(args, book):
    if len(args) >= 1:
        name, *_ = args
        name_find = book.find(name.lower())
        if name_find !=None:
            print(f"У контакта {name.capitalize()} день народження {name_find.birthday}")
        else:
            raise KeyError ("Контакт не знайдено. Спробуйте інше ім'я")
    else:
        raise ValueError ("Введіть ім'я")

@input_error
def birthdays(book):
    print("\nУ кого день народження наступного тижня:")
    for item in book.get_upcoming_birthdays():
        print(item)

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

@input_error
def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()