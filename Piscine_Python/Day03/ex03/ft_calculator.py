class calculator:
    """This is a calculator class"""
    def __init__(self, number: int) -> None:
        self.number = number

    def __str__(self) -> str:
        return f"{self.number}"

    def __repr__(self) -> str:
        return self.__str__()

    def __add__(self, object) -> None:
        #your code here

    def __mul__(self, object) -> None:
        #your code here

    def __sub__(self, object) -> None:
        #your code here

    def __truediv__(self, object) -> None:
        #your code here
