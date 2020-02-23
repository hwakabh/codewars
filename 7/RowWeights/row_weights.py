import sys


def row_weights(array):
    o = 0
    e = 0
    for i, n in enumerate(array):
        if i % 2 == 0:
            o += n
        else:
            e += n
    return (o, e)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        numbers = [int(i) for i in input('>>> Enter numbers to examine with comma-separated: ').split(',')]
        print(row_weights(array=numbers))
    else:
        sys.exit(1)
