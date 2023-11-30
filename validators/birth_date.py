import re

mask = r"^\s*(3[01]|[12][0-9]|0?[1-9])\.(1[012]|0?[1-9])\.((?:19|20)\d{2})\s*$"


def birth_date_validator(string):
    if not re.findall(mask, string):
        return False
    return True
