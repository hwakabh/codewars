import sys


def is_even(n):
    # float numbers are considered as un-even in this case
    if type(n) == float:
        return False
    else:
        return n % 2 == 0


if __name__ == "__main__":
    if len(sys.argv) == 2:
        inp = sys.argv[1]
        if '.' in inp:
            print(is_even(n=float(inp)))
        else:
            print(is_even(n=int(inp)))
    else:
        sys.exit(1)
