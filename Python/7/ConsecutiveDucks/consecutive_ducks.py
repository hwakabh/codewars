import sys
from math import log2


def consecutive_ducks(n):
    return not log2(n).is_integer()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(consecutive_ducks(n=int(sys.argv[1])))
    else:
        sys.exit(1)
