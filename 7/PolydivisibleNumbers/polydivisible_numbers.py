import sys


def polydivisible(x):
    for i in range(len(str(x))):
        num = str(x)[:(i+1)]
        if int(num) % len(num) != 0:
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(polydivisible(x=int(sys.argv[1])))
    else:
        sys.exit(1)
