import sys


def angle(n):
    # Each of internal angle == (180 * (n - 2)) / n
    return (180 * (n - 2))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(angle(n=int(sys.argv[1])))
    else:
        sys.exit(1)
