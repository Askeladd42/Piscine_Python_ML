import numpy as np


def give_bmi(
    height: np.ndarray,
    weight: np.ndarray
) -> np.ndarray:
    """returns a numpy array of BMI values calculated
    from the given height and weight arrays"""
    if height.shape != weight.shape:
        raise ValueError("Height and weight arrays must be of the same shape.")
    if not (np.issubdtype(height.dtype, np.number) and np.issubdtype(weight.dtype, np.number)):
        raise TypeError("Height and weight must be int or float.")
    return weight / (height ** 2)


def apply_limit(bmi: np.ndarray, limit: int) -> np.ndarray:
    if not np.issubdtype(bmi.dtype, np.number):
        raise TypeError("BMI values must be numeric.")
    return bmi > limit
