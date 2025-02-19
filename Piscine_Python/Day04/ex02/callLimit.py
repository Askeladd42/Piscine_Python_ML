def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: list, **kwargs: dict):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            return "No more calls available"
        return limit_function
    return callLimiter
