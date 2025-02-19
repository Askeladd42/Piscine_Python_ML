import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))


@dataclass
class Student:
    name: str = ""
    surname: str = ""

    def __post_init__(self):
        self.active = True
        self.login = self.name.lower() + "." + self.surname.lower()
        self.id = generate_id()

    def __str__(self):
        return f"Student {self.name} {self.surname} with ID {self.id}" + \
            f" and login {self.login}"

    def __repr__(self):
        return f"Student({self.name}, {self.surname})"
