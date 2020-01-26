import sys


def xo(s):
    return (s.count('x') + s.count('X')) == (s.count('o') + s.count('O'))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(xo(s=sys.argv[1]))
    else:
        sys.exit()
