import sys


def sum_mix(arr):
    s = 0
    for e in arr:
        s += int(e)
    return s


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inputs = [i for i in input('>>> Enter some elements to summarize with comma-separated: ').split(',')]
        print(sum_mix(arr=inputs))
    else:
        sys.exit(1)