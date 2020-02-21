import sys


def find(r):
    t = 0
    for i in r:
        t += (2 ** i)
    return t


if __name__ == "__main__":
    if len(sys.argv) == 1:
        rats = [int(c) for c in input('>>> Enter index of rats with comma separated').split(',')]
        print(find(r=rats))
    else:
        sys.exit(1)
