import numpy as np


def ft_statistics(*args: any, **kwargs: any) -> None:
    if not args:
        print("ERROR")
        return

    try:
        data = np.array(args, dtype=float)
    except ValueError:
        print("ERROR")
        return

    for key, value in kwargs.items():
        if value == "mean":
            print(f"{key} : {np.mean(data)}")
        elif value == "median":
            print(f"{key} : {np.median(data)}")
        elif value == "quartile":
            q25, q75 = np.percentile(data, [25, 75])
            print(f"{key} : [{q25}, {q75}]")
        elif value == "std":
            print(f"{key} : {np.std(data)}")
        elif value == "var":
            print(f"{key} : {np.var(data)}")
        else:
            print("ERROR")
