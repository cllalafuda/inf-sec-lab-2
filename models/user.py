from dataclasses import dataclass


@dataclass
class User:
    username: str
    password: int
    full_name: str
    birth_date: str
    birth_place: str
    phone_number: str
