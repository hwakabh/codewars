import sys


def find_it(seq):
    index = set(seq)
    for i in index:
        if seq.count(i) % 2 == 0:
            pass
        else:
            return i


if __name__ == '__main__':
    if len(sys.argv) == 1:
        array = [int(c) for c in input('>>> Enter sequence to check with comma-separated: ').split(',')]
        print(find_it(seq=array))
    else:
        sys.exit(1)

