import sys


def ordered_count(inp):
    i = sorted(set(inp), key=inp.index)
    return [(c, inp.count(c)) for c in i]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(ordered_count(inp=sys.argv[1]))
    else:
        sys.exit(1)
