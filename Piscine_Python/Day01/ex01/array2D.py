import numpy


def slice_me(family: list, start: int, end: int) -> list:
    return numpy.array(family)[start:end].tolist()
