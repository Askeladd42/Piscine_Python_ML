import numpy as np


class calculator:
    """This is a calculator class for vector operations with a scalar."""
    def __init__(self, numbers) -> None:
        self.numbers = np.array(numbers)

    def __add__(self, scalar: float) -> None:
        self.numbers = self.numbers + scalar
        print(self.numbers.tolist())

    def __mul__(self, scalar: float) -> None:
        self.numbers = self.numbers * scalar
        print(self.numbers.tolist())

    def __sub__(self, scalar: float) -> None:
        self.numbers = self.numbers - scalar
        print(self.numbers.tolist())

    def __truediv__(self, scalar: float) -> None:
        try:
            self.numbers = self.numbers / scalar
            print(self.numbers.tolist())
        except ZeroDivisionError:
            print("Error: division by zero")

    def __repr__(self):
        return str(self.numbers.tolist())
