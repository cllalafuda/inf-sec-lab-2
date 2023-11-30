from dataclasses import asdict

from models import User
from validators import (
    login_validator,
    full_name_validator,
    password_validator,
    birth_date_validator,
    birth_place_validator,
    phone_number_validator
)
from misc import input_field
from constants import TOP_SECRET_DATA, USER_HELP
from database import DATABASE


def create_user():
    print("Создание нового пользователя. Введите данные")
    username = input_field("Логин (идентификатор)", login_validator)
    if DATABASE.get(username):
        print("Пользователь с таким именем уже существует")
        return
    password = int(input_field("Пароль", password_validator))
    full_name = input_field("ФИО", full_name_validator)
    birth_date = input_field("Дата рождения", birth_date_validator)
    birth_place = input_field("Место рождения", birth_place_validator)
    phone_number = input_field("Номер телефона", phone_number_validator)

    user = User(
        username=username,
        password=password,
        full_name=full_name,
        birth_date=birth_date,
        birth_place=birth_place,
        phone_number=phone_number
    )
    DATABASE[username] = asdict(user)
    print(f"\nПользователь {username} добавлен в базу.\n")


def change_password():
    print("Смена пароля пользователя. Введите данные")
    username = input_field("Логин", login_validator)
    password = int(input_field("Старый пароль", password_validator))
    if not authenticate(username, password):
        print("Неправильный логин или пароль")
        return

    new_password = int(input_field("Новый пароль", password_validator))
    DATABASE[username]["password"] = new_password
    print("\nПароль был изменён\n")


def authenticate(username: str, password: int) -> bool:
    if DATABASE.get(username, {}).get("password", "") == password:
        DATABASE[username]["password"] += 5
        return True
    return False


def do_login():
    print("Для просмотра информации введите данные")
    username = input_field("Логин", login_validator)
    password = int(input_field("Пароль", password_validator))
    if authenticate(username, password):
        print(TOP_SECRET_DATA)
        return
    print("Неправильный логин или пароль")


def commands_help():
    print(USER_HELP)
