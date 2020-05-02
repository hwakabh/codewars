import sys


def find_all(array, n):
    return [i for i, j in enumerate(array) if j == n]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(i) for i in input('>>> Enter some numbers to find with comma-separated: ').split(',')]
        key = input('>>> Enter numbers to find: ')
        if len(key) != 1:
            print('Err, please provide a single number to find')
            sys.exit(1)
        else:
            print(find_all(array=inp, n=int(key)))
    else:
        sys.exit(1)

