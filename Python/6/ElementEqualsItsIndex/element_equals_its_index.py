import sys


def index_equals_value(arr):
    l, h = 0, len(arr) - 1
    while l <= h:
        m = (l + h) // 2

        if arr[m] < m:
            l = m + 1
        elif m < arr[m]:
            h = m - 1
        elif l != h:
            h = m
        else:
            return m
    # Case if not found
    return -1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(i) for i in input('>>> Enter numbers with comma-separated: ').split(',')]
        print(index_equals_value(arr=inp))
    else:
        sys.exit(1)
