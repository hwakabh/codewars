import sys


def derive(coefficient, exponent):
    return '{0}x^{1}'.format(coefficient * exponent, exponent - 1)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(derive(coefficient=int(sys.argv[1]), exponent=int(sys.argv[2])))
    else:
        sys.exit(1)
