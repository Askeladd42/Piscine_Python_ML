from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    def __init__(self, first_name):
        super().__init__(first_name)
        self._eyes = "brown"
        self._hairs = "dark"

    @property
    def eyes(self):
        return self._eyes

    @eyes.setter
    def eyes(self, color):
        self._eyes = color

    @property
    def hairs(self):
        return self._hairs

    @hairs.setter
    def hairs(self, color):
        self._hairs = color

    def set_eyes(self, color):
        self.eyes = color

    def get_eyes(self):
        return self.eyes

    def set_hairs(self, color):
        self.hairs = color

    def get_hairs(self):
        return self.hairs
