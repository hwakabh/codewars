import sys


def solve(s):
    l = s.replace('a', ' ').replace('e', ' ').replace('i', ' ').replace('o', ' ').replace('u', ' ')
    n = []
    for i in l.split():
        m = 0
        for c in i:
            m += ord(c) - 96
        n.append(m)
    return max(n)
 

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(solve(s=sys.argv[1]))
    else:
        sys.exit(1)
