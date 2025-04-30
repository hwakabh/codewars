import sys


def potatoes(p0, w0, p1):
    m = w0 * (p0 / 100)
    return int(round((w0 - m), 2) / ((100 - p1) / 100))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(potatoes(
            p0=int(sys.argv[1]),
            w0=int(sys.argv[2]),
            p1=int(sys.argv[3])
        ))
    else:
        sys.exit(1)
