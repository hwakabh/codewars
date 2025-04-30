import sys

def remove_char(s):
    return s[1:len(s)-1]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(remove_char(s=sys.argv[1]))
    else:
        sys.exit(1)