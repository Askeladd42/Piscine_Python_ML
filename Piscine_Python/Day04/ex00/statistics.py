def mean(data: list) -> float:
    return sum(data) / len(data)


def median(data: list) -> float:
    data.sort()
    n = len(data)
    mid = n // 2

    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2
    return data[mid]


def percentile(data: list, percentiles: list) -> tuple:
    data.sort()
    n = len(data)
    result = []

    for percentile in percentiles:
        index = (n - 1) * percentile / 100
        result.append(data[int(index)])

    return tuple(result)


def std(data: list) -> float:
    mean_data = mean(data)
    n = len(data)
    sum_squared_diff = sum((x - mean_data) ** 2 for x in data)
    return (sum_squared_diff / n) ** 0.5


def var(data: list) -> float:
    mean_data = mean(data)
    n = len(data)
    sum_squared_diff = sum((x - mean_data) ** 2 for x in data)
    return sum_squared_diff / n


def ft_statistics(*args: any, **kwargs: any) -> None:
    if not args:
        print("ERROR")
        return

    try:
        data = [float(arg) for arg in args]
    except ValueError:
        print("ERROR")
        return

    for key, value in kwargs.items():
        if value == "mean":
            print(f"mean : {mean(data)}")
        elif value == "median":
            print(f"median : {median(data)}")
        elif value == "quartile":
            q25, q75 = percentile(data, [25, 75])
            print(f"quartile : [{q25}, {q75}]")
        elif value == "std":
            print(f"std : {std(data)}")
        elif value == "var":
            print(f"var : {var(data)}")
        else:
            print("ERROR")
