import sys


def is_pangram(s):
    w = [c for c in s if c.isalpha()]
    return len(set(w)) >= 26


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter sentence to check it is a pangram or not: ')
        print(is_pangram(s=inp))
    else:
        sys.exit(1)
