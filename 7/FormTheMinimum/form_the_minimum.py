import sys


def min_value(digits):
    m = [str(i) for i in list(set(digits))]
    return int(''.join(sorted(m)))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        d = [int(i) for i in input('>>> Enter the numbers to form the minimum with comma-separated: ').split(',')]
        print(min_value(digits=d))
    else:
        sys.exit(1)
