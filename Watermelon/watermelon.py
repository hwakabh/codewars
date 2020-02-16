import sys


def divide(weight):
    if weight == 2:
        return False
    else:
        if (weight % 2) % 2 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(divide(weight=int(sys.argv[1])))
    else:
        sys.exit(1)
