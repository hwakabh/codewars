import sys


def index(array, n):
    if len(array) - 1 < n:
        return -1
    else:
        return array[n] ** n


if __name__ == "__main__":
    if len(sys.argv) == 1:
        num = [int(i) for i in input('>>> Enter numbers to find N-th power with comma-separated: ').split(',')]
        N = int(input('>>> Enter number for N: '))
        print(index(array=num, n=N))
    else:
        sys.exit(1)
