import sys


def friends(x):
    f = []
    for n in x:
        if len(n) == 4:
            f.append(n)
    return f

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        print(friends(x=sys.argv[1:]))