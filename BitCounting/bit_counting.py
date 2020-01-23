import sys


def countBits(n):
    bits = bin(n).replace('0b','')
    c = 0
    for b in bits:
        if b == '1':
            c += 1
    return c


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(countBits(n=int(sys.argv[1])))
    else:
        sys.exit(1)
