import sys


def abbrevName(name):
    return '{0}.{1}'.format(name.split()[0][0], name.split()[1][0]).upper()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        n = input('>>> Enter your name: ')
        print(abbrevName(name=n))
    else:
        sys.exit(1)
