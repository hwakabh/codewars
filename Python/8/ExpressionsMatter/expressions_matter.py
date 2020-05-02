import sys


def expression_matter(a, b, c):
    num = [
        a * b * c,
        a + b + c,
        a * (b + c),
        a + b * c,
        a * b + c,
        (a + b) * c,
    ]
    return max(num)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(expression_matter(a=int(sys.argv[1]), b=int(sys.argv[2]), c=int(sys.argv[3])))
    else:
        sys.exit(1)
