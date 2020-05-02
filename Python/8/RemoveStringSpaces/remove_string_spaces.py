import sys


def no_space(x):
    return x.replace(' ', '')


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter string to remove spaces: ')
        print(no_space(x=inp))
    else:
        sys.exit(1)
