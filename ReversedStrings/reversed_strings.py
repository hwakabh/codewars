import sys


def solutions(string):
    return ''.join(sorted(string, key=string.index, reverse=True))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(solutions(string=sys.argv[1]))
    else:
        sys.exit(1)
