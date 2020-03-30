import sys


def two_sort(array):
    f = sorted(array)[0]
    return ''.join('{0}'.format(c + '***') for c in f)[:-3]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter vector of string to sort with comma-separated: ').split(',')
        print(two_sort(array=inp))
    else:
        sys.exit(1)
