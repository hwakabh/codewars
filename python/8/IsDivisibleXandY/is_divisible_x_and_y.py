import sys


def is_divisible(n, x, y):
    return n % x == 0 and n % y == 0


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(is_divisible(n=int(sys.argv[1]), x=int(sys.argv[2]), y=int(sys.argv[3])))
    else:
        sys.exit(1)
