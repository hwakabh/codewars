import sys


def odd_one_out(s):
    l = {}
    for c in s:
        if c in l:
            del l[c]
        else:
            l[c] = None
    return list(l.keys())
    # # List would be timeout
    # l = []
    # for c in s:
    #     if c in l:
    #         l.remove(c)
    #     else:
    #         l.append(c)
    # return l


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        w = ' '.join(sys.argv[1:])
        print(odd_one_out(s=w))
    else:
        sys.exit(1)
