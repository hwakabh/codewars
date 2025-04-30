import sys


def make_nagative(number):
    return number.__abs__() * (-1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(make_nagative(number=int(sys.argv[1])))
    else:
        sys.exit(1)
