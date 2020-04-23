import sys


def isPP(n):
    # Get divisors
    d = [i for i in range(1,n+1) if n % i == 0]
    # print('>>> n: {} and its divisors {}'.format(n, d))
    for r in d:
        for k in range(2, n):
            if r ** k == n:
                # print('n: {} = {}^{}'.format(n, r, k))
                return [r, k]
    return None


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(isPP(n=int(sys.argv[1])))
    else:
        sys.exit(1)
