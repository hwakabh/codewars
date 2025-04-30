import sys


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(xo(s=sys.argv[1]))
    else:
        sys.exit()
