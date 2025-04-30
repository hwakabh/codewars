import sys


def number(lines):
    return ['{0}: {1}'.format(i+1, l) for i, l in enumerate(lines)]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter some lines to test: ')
        print(number(lines=inp))
    else:
        sys.exit(1)
