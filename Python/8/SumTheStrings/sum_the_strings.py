import sys


def sum_str(a, b):
    return str(int(a or 0) + int(b or 0))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(sum_str(a=sys.argv[1], b=sys.argv[2]))
    else:
        sys.exit(1)
