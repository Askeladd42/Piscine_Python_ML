def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: list, **kwargs: dict):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            print(
                f"Error: <function {function.__name__} "
                f"at {hex(id(function))}> call too many times")
        return limit_function
    return callLimiter
