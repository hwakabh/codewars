import sys


def digitize(n):
    return [int(c) for c in str(n)[::-1]]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(digitize(n=int(sys.argv[1])))
    else:
        sys.exit(1)
