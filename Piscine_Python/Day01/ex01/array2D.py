import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """returns a slice of the given list from start to end"""
    print(f"My shape is : {np.array(family).shape}")
    print(f"My new shape is : {np.array(family)[start:end].shape}")
    return np.array(family)[start:end].tolist()
