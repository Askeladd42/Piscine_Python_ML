import sys
from ft_filter import ft_filter

def main():
    # your tests and your error handling
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Exactly 2 arguments are required")

        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("The second argument must be an integer")

        if not isinstance(S, str):
            raise AssertionError("The first argument must be a string")

        # Use ft_filter to filter words longer than N
        result = list(ft_filter(lambda word: len(word) > N, S.split()))
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")

if __name__ == "__main__":
    main()