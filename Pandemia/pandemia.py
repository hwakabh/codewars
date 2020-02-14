import sys


def infected(s):
    s = [p for p in s.split('X') if not p == '']
    if s == []:
        return 0
    else:
        e = ''.join([l.replace('0', '1') if l.count('1') != 0 else l for l in s])
        i = e.count('1')
        return (100 * i/len(e))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(infected(s=sys.argv[1]))
    else:
        sys.exit(1)
