import sys


def halving_sum(n):
    if n == 1:
        return 1
    else:
        return n + halving_sum(n // 2)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(halving_sum(n=int(sys.argv[1])))
    else:
        sys.exit(1)
