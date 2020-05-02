import sys


def dominator(arr):
    a = set(arr)
    for i in a:
        if arr.count(i) > (len(arr) // 2):
            return i
    return -1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(c) for c in input('>>> Enter integer numbers to dominate with comma-separated: ').split(',')]
        print(dominator(arr=inp))
    else:
        sys.exit(1)
