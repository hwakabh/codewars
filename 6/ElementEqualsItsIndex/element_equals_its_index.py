import sys


def index_equals_value(arr):
    for i, x in enumerate(arr):
        if arr[i] == i:
            return x
    return -1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(i) for i in input('>>> Enter numbers with comma-separated: ').split(',')]
        print(index_equals_value(arr=inp))
    else:
        sys.exit(1)
