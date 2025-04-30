import sys


def triple_trouble(one, two, three):
    s = ''
    for i in range(len(one)):
        s += one[i]
        s += two[i]
        s += three[i]
    return s


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(triple_trouble(one=sys.argv[1], two=sys.argv[2], three=sys.argv[3]))
    else:
        sys.exit(1)
