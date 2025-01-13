import sys

NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/'
}

def to_morse_code(text):
    morse_code = []
    for char in text.upper():
        if char in NESTED_MORSE:
            morse_code.append(NESTED_MORSE[char])
        else:
            raise AssertionError(f"Character '{char}' cannot be converted to Morse code")
    return ' '.join(morse_code)

def main():
    # your tests and your error handling
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Exactly 1 argument is required")
        
        input_string = sys.argv[1]
        if not isinstance(input_string, str):
            raise AssertionError("The argument must be a string")
        
        morse_code = to_morse_code(input_string)
        print(morse_code)
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()