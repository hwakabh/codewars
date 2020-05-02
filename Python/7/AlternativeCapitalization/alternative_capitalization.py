import sys


def capitalize(s):
    e = ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])
    o = ''.join([c.upper() if i % 2 != 0 else c.lower() for i, c in enumerate(s)])
    return [e, o]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(capitalize(s=sys.argv[1]))
    else:
        sys.exit(1)
