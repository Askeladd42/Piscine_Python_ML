import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """returns a slice of the given list from start to end"""
    try:
        if not isinstance(family, list):
            raise TypeError("Please provide a list")
        if not isinstance(start, int) or not isinstance(end, int):
            raise TypeError("Please provide integers for start and/or end")
        if start < 0 or end > len(family):
            raise ValueError("Invalid start or end indices")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end].shape}")
        return np.array(family)[start:end].tolist()
    except Exception as e:
        return e
