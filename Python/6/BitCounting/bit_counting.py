import sys


def countBits(n):
    bits = bin(n).replace('0b','')
    return bits.count('1')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(countBits(n=int(sys.argv[1])))
    else:
        sys.exit(1)
