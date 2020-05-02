import sys


def nb_year(p0, percent, aug, p):
    n = p0
    c = 0
    while n < p:
        n = n + n * (percent / 100) + aug
        c += 1
    return c


if __name__ == "__main__":
    if len(sys.argv) == 5:
        print(nb_year(p0=int(sys.argv[1]), percent=int(sys.argv[2]), aug=int(sys.argv[3]), p=int(sys.argv[4])))
    else:
        sys.exit(1)
