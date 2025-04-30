import sys


def paperwork(n, m):
    if (n < 0) or (m < 0):
        return 0
    else:
        return n * m


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(paperwork(n=int(sys.argv[1]), m=int(sys.argv[2])))
    else:
        sys.exit(1)
