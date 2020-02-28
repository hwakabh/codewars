import sys


def sum_str(a, b):
    if a and b:
        return str(int(a) + int(b))
    elif a:
        return a
    elif b:
        return b
    else:
        return '0'


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(sum_str(a=sys.argv[1], b=sys.argv[2]))
    else:
        sys.exit(1)
