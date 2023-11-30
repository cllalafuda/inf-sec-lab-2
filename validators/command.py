from constants import COMMANDS


def command_validator(string):
    if string not in COMMANDS:
        return False
    return True
