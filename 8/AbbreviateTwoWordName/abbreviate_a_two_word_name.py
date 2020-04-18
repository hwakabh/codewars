import sys


def abbrevName(name):
    f, l = name.upper().split()
    return '{0}.{1}'.format(f[0], l[0])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        n = input('>>> Enter your name: ')
        print(abbrevName(name=n))
    else:
        sys.exit(1)
