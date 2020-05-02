import sys


def seven(m):
    c = 0
    while m >= 100:
        x = m // 10
        y = m % 10
        m = x - (y * 2)
        c += 1
    return (m, c)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(seven(m=int(sys.argv[1])))
    else:
        sys.exit(1)
