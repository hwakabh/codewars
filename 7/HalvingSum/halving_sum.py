import sys


def halving_sum(n):
    if n <= 2:
        return 1
    else:
        s = n
        d = 2
        while d <= n // 2:
            s += n // d
            d *= 2
        return s + 1


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(halving_sum(n=int(sys.argv[1])))
    else:
        sys.exit(1)
