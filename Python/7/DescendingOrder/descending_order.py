import sys


def descending_order(num):
    r = sorted(str(num), reverse=True)
    return int(''.join(r))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(descending_order(num=int(sys.argv[1])))
    else:
        sys.exit(1)
