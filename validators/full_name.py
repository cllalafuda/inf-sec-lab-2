def full_name_validator(string):
    if not string:
        return False
    if len(string.split()) < 2:
        return False
    return True
