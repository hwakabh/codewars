import sys


def divisors(n):
    d = [n / i for i in range(1, n+1) if n % i == 0]
    return len(d)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(divisors(n=int(sys.argv[1])))
    else:
        sys.exit(1)
