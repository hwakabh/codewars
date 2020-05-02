import sys


def breakChocolate(n, m):
    if (n == 0) and (m == 0):
        return 0
    else:
        return (n * m) -1


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(breakChocolate(n=int(sys.argv[1]), m=int(sys.argv[2])))
    else:
        sys.exit(1)
