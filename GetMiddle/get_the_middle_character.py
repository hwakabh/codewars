import sys

def get_middle(s):
    l = len(s)
    r = int(l % 2)
    if r == 1:
        c = s[int(l / 2)]
    else:
        c = s[int(l / 2 - 1):int(l / 2 + 1)]
    return c
 

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_middle(s=sys.argv[1]))
    else:
        sys.exit(1)
