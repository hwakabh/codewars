import sys


def get_real_floor(n):
    if n in range(1,13):
        return n - 1
    elif n >= 14:
        return n -2
    else:
        return n


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(get_real_floor(n=int(sys.argv[1])))
    else:
        sys.exit(1)
