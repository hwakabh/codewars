import sys


def past(h, m, s):
    sec = h * 60 * 60 + m * 60 + s
    return sec * 1000


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(past(h=int(sys.argv[1]), m=int(sys.argv[2]), s=int(sys.argv[3])))
    else:
        sys.exit(1)
