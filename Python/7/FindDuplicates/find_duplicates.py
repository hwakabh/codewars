import sys


def duplicates(array):
    d = []
    for i in range(len(array)):
        if (array[i] in array[:i]) and (array[i] not in d):
            d.append(array[i])
    return d


if __name__ == "__main__":
    if len(sys.argv) == 1:
        a = input('>>> Enter some elements for finding duplications with comma-separated').split(',')
        print(duplicates(array=a))
    else:
        sys.exit(1)
