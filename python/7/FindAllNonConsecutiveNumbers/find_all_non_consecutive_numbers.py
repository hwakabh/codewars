import sys


def all_non_consecutive(arr):
    exp = []
    for i in range(len(arr)):
        if i > 0:
            if (arr[i] - arr[i - 1] != 1):
                exp.append({'i': i, 'n': arr[i]})
    return exp


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(i) for i in input('>>> Enter numbers of array with comma-separated: ').split(',')]
        print(all_non_consecutive(arr=inp))
    else:
        sys.exit(1)
