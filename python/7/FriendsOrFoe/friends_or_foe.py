import sys


def friends(x):
    return [f for f in x if len(f) == 4]

if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        print(friends(x=sys.argv[1:]))