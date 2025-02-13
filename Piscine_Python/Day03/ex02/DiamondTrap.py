from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""
    def __init__(self, first_name=None, is_alive=True):
        """Initialize the King"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "blue"
        self.hair = "black"
