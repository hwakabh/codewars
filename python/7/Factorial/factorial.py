import sys


def factorial(n):
    if n >= 1:
        f = 1
        for i in range(n):
            f *= (i + 1)
        return f
    else:
        return 1


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(factorial(n=int(sys.argv[1])))
    else:
        sys.exit(1)
