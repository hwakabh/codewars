import sys


def divisors(integer):
    d = [i for i in range(2, integer) if integer % i == 0]
    if len(d) == 0:
        return '{} is prime'.format(integer)
    else:
      return d


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(divisors(integer=int(sys.argv[1])))
    else:
        sys.exit(1)
