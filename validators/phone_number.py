def phone_number_validator(string: str):
    if not string:
        return False
    if not string.isdigit():
        return False
    if len(string) != 11:
        return False

    return True
