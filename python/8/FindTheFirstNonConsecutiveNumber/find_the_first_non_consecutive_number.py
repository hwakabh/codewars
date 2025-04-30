import sys


def first_non_consecutive(arr):
    for j in range(len(arr)):
        if j == 0:
            pass
        else:
            if (arr[j] - arr[j - 1] != 1):
                return arr[j]
    return None


if __name__ == "__main__":
    if len(sys.argv) == 1:
        num = [int(i) for i in input('>>> Enter numbers to examine whether consecutive or not with comma-separated: ').split(',')]
        print(first_non_consecutive(arr=num))
    else:
        sys.exit(1)
