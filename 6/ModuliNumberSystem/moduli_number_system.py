import sys
import fractions
import functools


def fromNb2Str(n, modsys):
    # Reject if elements of modsys is not pairwise co-prime
    def gcd(*numbers):
        return functools.reduce(fractions.gcd, numbers)
    for m in modsys:
        for i in range(len(modsys)):
            if m == modsys[i]:
                continue
            if gcd(m, modsys[i]) != 1:
                return 'Not applicable'
    # Reject if products of modsys is smaller than n
    p = 1
    for m in modsys:
        p *= m
    if p < n:
        return 'Not applicable'
    else:
        return ''.join(['-{}-'.format(n % c) for c in modsys])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        N = int(input('>>>> Enter the numbers to divide as prime number: '))
        numbers = [int(c) for c in input('>>> Enter the numbers as moduli system with comma-separated: ').split(',')]
        print(fromNb2Str(n=N, modsys=numbers))
    else:
        sys.exit(1)
