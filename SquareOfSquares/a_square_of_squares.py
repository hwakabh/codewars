import sys
import math


def is_square(n):
    if (n >= 0) and (int(math.sqrt(n)) ** 2 == n):
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(is_square(n=int(sys.argv[1])))
    else:
        sys.exit(1)
