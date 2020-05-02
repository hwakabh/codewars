import sys


def max_multiple(divisor, bound):
    return (bound // divisor) * divisor


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(max_multiple(divisor=int(sys.argv[1]), bound=int(sys.argv[2])))
    else:
        sys.exit(1)
