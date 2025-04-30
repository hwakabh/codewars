import sys


def find_short(s):
    wc = [len(w) for w in s.split()]
    return min(wc)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        p = input('>>> Enter sentences to counting shorted words: ')
        print(find_short(s=p))
    else:
        sys.exit(1)
