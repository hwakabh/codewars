import sys


# a = 123.toString()
def to_string(n):
    return str(n)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(to_string(n=int(sys.argv[1])))
    else:
        sys.exit(1)
