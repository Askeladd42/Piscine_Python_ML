from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the King"""
    def __init__(self, first_name=None, is_alive=True):
        """Initialize the King"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hair = "dark"

    @property
    def eyes(self):
        """Get the eye color of the King"""
        return self.eyes

    @property
    def hair(self):
        """Get the hair color of the King"""
        return self.hair

    @eyes.setter
    def eyes(self, color):
        """Set the eye color of the King"""
        self.eyes = color

    @hair.setter
    def hair(self, color):
        """Set the hair color of the King"""
        self.hair = color
