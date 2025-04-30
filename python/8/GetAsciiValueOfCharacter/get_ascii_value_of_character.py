import sys


def get_ascii(c):
    return ord(c)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if len(sys.argv[1]) != 1:
            print('Please enter a character instead of word/sentence')
            sys.exit(1)
        else:
           print(get_ascii(c=sys.argv[1]))
    else:
        sys.exit(1)
 