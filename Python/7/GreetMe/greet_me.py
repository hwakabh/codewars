import sys


def greet(name):
    return 'Hello {}!'.format(name.capitalize())


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(greet(name=sys.argv[1]))
    else:
        sys.exit(1)
