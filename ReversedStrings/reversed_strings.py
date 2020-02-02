import sys


def solutions(string):
    return string[::-1]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(solutions(string=sys.argv[1]))
    else:
        sys.exit(1)
