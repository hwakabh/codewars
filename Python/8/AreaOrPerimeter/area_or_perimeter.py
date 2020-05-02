import sys


def area_or_perimeter(l, w):
    # As problem-set condition, we could assume that:
    # it is a square if its length and width are equal, otherwise it is a rectangle.
    if l == w:
        return l * w
    else:
        return (l + w) * 2


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(area_or_perimeter(l=int(sys.argv[1]), w=int(sys.argv[2])))
    else:
        sys.exit(1)
