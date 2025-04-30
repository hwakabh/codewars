import sys


def next_num(n):
    def is_polydivisible(m):
        d = len(str(m))
        for i in range(d):
            if not int(str(m)[:i+1]) % (i+1) == 0:
                return False
        return True

    opr = n + 1
    while True:
        if not is_polydivisible(m=opr):
            opr += 1
        else:
            break
    return opr


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(next_num(n=int(sys.argv[1])))
    else:
        sys.exit(1)
