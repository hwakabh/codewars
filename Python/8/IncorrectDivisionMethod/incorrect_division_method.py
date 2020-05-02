import sys


def divide_numbers(x, y):
    return float(x) / y


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(divide_numbers(x=int(sys.argv[1]), y=int(sys.argv[2])))
    else:
        sys.exit(1)
