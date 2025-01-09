import sys

import string

def count_characters(s):
    counts = {
        'upper': 0,
        'lower': 0,
        'puncts': 0,
        'spaces': 0,
        'digits': 0
    }
    
    for char in s:
        if char.isupper():
            counts['upper'] += 1
        elif char.islower():
            counts['lower'] += 1
        elif char in string.punctuation:
            counts['puncts'] += 1
        elif char.isspace():
            counts['spaces'] += 1
        elif char.isdigit():
            counts['digits'] += 1
    
    return counts


def main():
    # your tests and your error handling
    if len(sys.argv) < 2:
        input_string = input("Please enter a string: ")
    elif len(sys.argv) > 2:
        AssertionError("Too many arguments")
    else:
        input_string = sys.argv[1]
    counts = count_characters(input_string)
    
    print(f"{counts['uppercase']} upper letters")
    print(f"{counts['lowercase']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")



if __name__ == "__main__":
    main()