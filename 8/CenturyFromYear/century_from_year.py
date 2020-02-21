import sys
import math

def century(year):
    return math.ceil(year / 100)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(century(year=int(sys.argv[1])))
    else:
        sys.exit(1)