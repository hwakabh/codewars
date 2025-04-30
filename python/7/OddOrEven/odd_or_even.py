import sys


def oddOrEven(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'


if __name__ == "__main__":
    if len(sys.argv) == 1:
        array = [int(a) for a in input('>>> Enter the numbers with comma-separated: ').split(',')]
        print(oddOrEven(arr=array))
    else:
        sys.exit(1)