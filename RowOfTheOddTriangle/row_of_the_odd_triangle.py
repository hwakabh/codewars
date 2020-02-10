import sys


def odd_row(n):
    f = n ** 2 - (n - 1)
    e = (n + 1) ** 2 - (n + 1 - 1)
    return list(range(f, e, 2))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(odd_row(n=int(sys.argv[1])))
    else:
        sys.exit(1)
