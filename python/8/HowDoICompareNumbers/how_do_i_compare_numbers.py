import sys


def what_is(x):
    if x == 42:
        return 'everything'
    elif x == 42 * 42:
        return 'everything squared'
    else:
        return 'nothing'


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(what_is(x=int(sys.argv[1])))
    else:
        sys.exit(1)
