import sys
import math


def is_square(n):
    # Ignore negative value
    if n < 0:
        return False
    # If positive value, get square root
    r = int(math.sqrt(n))
    if r ** 2 == n:
        return True
    else:
        return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(is_square(n=int(sys.argv[1])))
    else:
        sys.exit(1)
