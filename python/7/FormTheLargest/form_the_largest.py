import sys


def max_number(n):
    return int(''.join(sorted(str(n), reverse=True)))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(max_number(n=sys.argv[1]))
    else:
        sys.exit(1)