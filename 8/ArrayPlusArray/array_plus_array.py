import sys


def array_plus_array(arr1, arr2):
    return sum(arr1) + sum(arr2)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        x = [int(i) for i in input('>>> Enter elements of first array with comma-separated: ').split(',')]
        y = [int(j) for j in input('>>> Enter elements of second array with comma-separated: ').split(',')]
        print(array_plus_array(arr1=x, arr2=y))
    else:
        sys.exit(1)
