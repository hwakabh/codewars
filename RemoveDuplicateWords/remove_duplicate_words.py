import sys


def remove_duplicate_words(s):
    w = s.split()
    return ' '.join(sorted(set(w), key=w.index))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        words = ' '.join(sys.argv[1:])
        print(remove_duplicate_words(s=words))
    else:
        sys.exit(1)