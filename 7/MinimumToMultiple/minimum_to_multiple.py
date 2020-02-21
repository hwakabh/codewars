import sys


def minimum(a, x):
    m = x * (a // x + 1)
    n = x * (a // x)
    if (m - a) > (a - n):
        return (a - n)
    else:
        return (m - a)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(minimum(
            a=int(sys.argv[1]),
            x=int(sys.argv[2])))
    else:
        sys.exit(1)