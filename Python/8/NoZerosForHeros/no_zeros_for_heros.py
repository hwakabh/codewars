import sys


def no_boring_zeros(n):
    if n == 0:
        return n
    else:
        while True:
            if n % 10 != 0:
                return int(n)
            else:
                n /= 10


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(no_boring_zeros(n=int(sys.argv[1])))
    else:
        sys.exit(1)
