import sys


def persistence(n):
    if n <= 9:
        return 0
    else:
        ds = n
        c = 0
        while ds >= 10:
            p = 1
            for d in str(ds):
                p *= int(d)
            ds = p
            c += 1
        return c


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(persistence(n=int(sys.argv[1])))
    else:
        sys.exit(1)
