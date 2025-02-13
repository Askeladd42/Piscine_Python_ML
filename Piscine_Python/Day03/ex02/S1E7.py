from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""
    def __init__(self, first_name=None, is_alive=True):
        """Initialize the Baratheon family"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    def __str__(self):
        """Return the name of the character"""
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        """Return the representation of the character"""
        return self.__str__()


class Lannister(Character):
    """Representing the Lannister family"""
    def __init__(self, first_name=None, is_alive=True):
        """Initialize the Lannister family"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hair = "light"

    def __str__(self):
        return f"{self.first_name} {self.family_name}"

    def __repr__(self):
        return self.__str__()

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """Class method to create a Lannister character"""
        return cls(first_name, is_alive)
