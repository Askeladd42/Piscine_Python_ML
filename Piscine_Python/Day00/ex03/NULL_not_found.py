def NULL_not_found(object: any) -> int:
    #  your code here
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif object != object:  # This is the only way to check for NaN
        print(f"Cheese: {object} {type(object)}")
        return 0
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif object == '':
        print(f"Empty: {object} {type(object)}")
        return 0
    elif object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
