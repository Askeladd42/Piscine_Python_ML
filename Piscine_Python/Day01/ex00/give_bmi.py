def give_bmi(
    height: list[int | float],
    weight: list[int | float]
) -> list[int | float]:
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")
    for h, w in zip(height, weight):
        if not isinstance(h, (int, float)) or not isinstance(w, (int, float)):
            raise TypeError("Height and weight must be int or float.")
    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI values must be int or float.")
    return [b > limit for b in bmi]
