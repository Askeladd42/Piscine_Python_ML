import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    name: str = ""
    surname: str = ""
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        self.login = self.name.lower() + "." + self.surname.lower()

    def __str__(self):
        return f"Student {self.name} {self.surname} with ID {self.id}" + \
               f" and login {self.login}"

    def __repr__(self):
        return f"Student({self.name}, {self.surname})"
