import sys


def solve(a, b):
    da = ''.join(c for c in a if not c in b)
    db = ''.join(c for c in b if not c in a)
    return da + db


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(solve(a=sys.argv[1], b=sys.argv[2]))
    else:
        sys.exit(1)
