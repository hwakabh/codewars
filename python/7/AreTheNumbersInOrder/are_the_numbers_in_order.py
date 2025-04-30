import sys


def in_asc_order(arr):
    return sorted(arr) == arr


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(c) for c in input('>>> Enter array of numbers to check with comma-separated: ').split(',')]
        print(in_asc_order(arr=inp))
    else:
        sys.exit(1)
