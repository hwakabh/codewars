import sys


def add_letters(letters):
    s = 0
    if len(letters) == 0:
        return 'z'
    else:
        for c in letters:
            s += (ord(c) - 96)
        return chr((s - 1) % 26 + 97)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        l = [i for i in input('>>> Enter alphabets to sum with comma-separated: ').split(',')]
        print(add_letters(l))
    else:
        sys.exit(1)
