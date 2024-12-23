def all_thing_is_obj(object: any) -> int:
#your code here
    content = ""
    if type(object) == str:
        content = object + " is in the kitchen"
    elif type(object) == list:
        content = "List"
    elif type(object) == tuple:
        content = "Tuple"
    elif type(object) == set:
        content = "Set"
    elif type(object) == dict:
        content = "Dict"
    else:
        content = "unknown"
    if content == "unknown":
        print("Type not found")
    else:
        print(f"{content} : {type(object)}")
    return 42