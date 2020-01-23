import sys


def toJadenCase(string):
    words = [w.capitalize() for w in string.split(' ')]
    return ' '.join(words)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        sentence = ' '.join(sys.argv[1:])
        print(toJadenCase(string=sentence))
