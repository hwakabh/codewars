import sys


def array_diff(a, b):
    diff = []
    for i in a:
        if not i in b:
          diff.append(i)
    return diff


if __name__ == "__main__":
    if len(sys.argv) == 1:
        first = input('Enter first array elements: ').split(',')
        second = input('Enter second array elements: ').split(',')
        print(array_diff(a=first, b=second))
    else:
        sys.exit(1)