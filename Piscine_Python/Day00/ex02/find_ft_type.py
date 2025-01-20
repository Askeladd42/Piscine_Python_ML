def all_thing_is_obj(object: any) -> int:
    # your code here
    content = ""
    if type(object) is str:
        content = object + " is in the kitchen"
    elif type(object) is list:
        content = "List"
    elif type(object) is tuple:
        content = "Tuple"
    elif type(object) is set:
        content = "Set"
    elif type(object) is dict:
        content = "Dict"
    else:
        content = "unknown"
    if content == "unknown":
        print("Type not found")
    else:
        print(f"{content} : {type(object)}")
    return 42
