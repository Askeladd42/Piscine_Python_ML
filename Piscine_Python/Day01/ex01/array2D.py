import numpy


def slice_me(family: list, start: int, end: int) -> list:
    """returns a slice of the given list from start to end"""
    return numpy.array(family)[start:end].tolist()
