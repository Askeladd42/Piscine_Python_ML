import sys
from ft_filter import ft_filter


def main():
    # your tests and your error handling
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        S = sys.argv[1]
        try:
            N = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        if not isinstance(S, str):
            raise AssertionError("the arguments are bad")

        # Use ft_filter to filter words longer than N
        result = list(ft_filter(lambda word: len(word) >= N, S.split()))
        print(result)
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
