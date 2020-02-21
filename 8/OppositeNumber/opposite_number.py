import sys


def opposite(number):
    return number * (-1)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(opposite(number=int(sys.argv[1])))
    else:
        sys.exit(1)
