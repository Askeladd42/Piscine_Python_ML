import numpy as np


def give_bmi(height: list[int | float],
             weight: list[int | float]
             ) -> list[int | float]:
    """Calculates the BMI of a person based on their height and weight.
    The formula is weight / (height ** 2) and uses the metric system."""
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    height_array = np.array(height)
    weight_array = np.array(weight)

    if not (np.issubdtype(height_array.dtype, np.number)
            and np.issubdtype(weight_array.dtype, np.number)):
        raise TypeError("Height and weight must be int or float.")

    bmi_array = weight_array / (height_array ** 2)
    return bmi_array.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Returns a list of booleans indicating whether the BMI is above the
    given limit."""
    bmi_array = np.array(bmi)

    if not np.issubdtype(bmi_array.dtype, np.number):
        raise TypeError("BMI values must be int or float.")

    limit_array = bmi_array > limit
    return limit_array.tolist()
