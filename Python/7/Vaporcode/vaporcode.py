import sys


def vaporcode(s):
    return '  '.join(s.replace(' ', '').upper())


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter sentence to vapor : ')
        print(vaporcode(s=inp))
    else:
        sys.exit(1)
