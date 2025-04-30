import sys


def array_madness(a, b):
    return sum([i ** 2 for i in a]) > sum([j ** 3 for j in b])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = [int(i) for i in input('>>> Enter first array: ')]
        y = [int(j) for j in input('>>> Enter second array: ')]
        print(array_madness(a=x, b=y))
    else:
        sys.exit(1)
        