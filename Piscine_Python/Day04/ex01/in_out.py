def square(x: int | float) -> int | float:
    """Returns the square of the argument."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns the exponentiation of the argument by itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that takes no arguments
    and returns the result of the function
    passed as an argument to outer."""
    count = [0]  # Settled as a list to avoid using global variables.
    result = [x]

    def inner() -> float:
        count[0] += 1
        result[0] = function(result[0])
        return result[0]

    return inner
