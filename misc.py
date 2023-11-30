import sys
from typing import Callable

from validators import command_validator


def get_command():
    command = input_field("Введите команду. h для справки по всем командам", command_validator)
    return command


def input_field(prompt: str, validator: Callable):
    raw_input = ""
    while not validator(raw_input.strip()):
        raw_input = input(f"{prompt} > ")
    if raw_input == "q":
        print("Выполнение программы было остановлено")
        sys.exit(0)
    return raw_input.strip()