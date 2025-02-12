from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name=None, last_name=None, status=None):
        super().__init__(first_name, last_name, status)
        self.family_name = "Baratheon"
        self.house_words = "Ours is the Fury"


class Lannister(Character):
    def __init__(self, first_name=None, last_name=None, status=None):
        super().__init__(first_name, last_name, status)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar"


def create_lannister(first_name, last_name, status):
    return Lannister(first_name, last_name, status)
