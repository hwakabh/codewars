import sys


def check(seq, elem):
    return elem in seq


if __name__ == "__main__":
    if len(sys.argv) == 1:
        e = input('>>> Enter elements for checking: ')
        s = input('>>> Enter key for find: ')
        print(check(seq=s, elem=e))
    else:
        sys.exit(1)
