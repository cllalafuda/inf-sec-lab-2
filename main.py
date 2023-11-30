from dataclasses import asdict

from models import User
from user_methods import create_user, change_password, do_login, commands_help
from misc import get_command

from database import DATABASE


DATABASE["user1"] = (
    # Пример данных в in-memory key-value базе данных
    asdict(User(
        username="user1",
        password=12345670,
        full_name="Иванов Иван Иванович",
        birth_date="08.10.2005",
        birth_place="Москва, Россия",
        phone_number="89660386453"
    ))
)

COMMANDS_MAPPING = {
    "c": create_user,
    "ch": change_password,
    "l": do_login,
    "h": commands_help
}


def main():
    while True:
        command = get_command()
        COMMANDS_MAPPING[command]()


if __name__ == '__main__':
    main()
