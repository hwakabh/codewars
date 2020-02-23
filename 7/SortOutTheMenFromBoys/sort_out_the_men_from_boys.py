import sys


def men_from_boys(arr):
    e = sorted([i for i in arr if i % 2 == 0])
    o = sorted([i for i in arr if i % 2 != 0], reverse=True)
    return sorted(set(e), key=e.index) + sorted(set(o), key=o.index)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        g = [int(c) for c in input('Enter array to split odd/even with comma-separated: ')]
        print(men_from_boys(arr=g))
    else:
        sys.exit(1)
