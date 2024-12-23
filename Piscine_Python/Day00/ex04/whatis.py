import sys

def whatis(object: any) -> str:
    if isinstance(object, (int)):
        if object % 2 == 0:
            return "I'm Even."
        else:
            return "I'm Odd."

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
    
        input_value = sys.argv[1]
        try:
            input_value = int(input_value)
        except ValueError:
            raise AssertionError("argument is not an integer")
    
        print(whatis(input_value))
    except AssertionError as e:
        print(f"AssertionError: {e}")