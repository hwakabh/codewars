import sys


def litres(time):
    return int(time * 0.5 // 1)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(litres(time=int(sys.argv[1])))
    else:
        sys.exit(1)
