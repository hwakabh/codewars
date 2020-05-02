import sys


def lottery(s):
    f = [c for c in s if c.isdigit()]
    if f == []:
        return 'One more run!'
    else:
        return ''.join(sorted(set(f), key=f.index))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(lottery(s=sys.argv[1]))
    else:
        sys.exit(1)