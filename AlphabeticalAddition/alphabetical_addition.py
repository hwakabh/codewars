import sys


def add_letters(letters):
    s = 0
    if len(letters) == 0:
        return 'z'
    else:
        for c in letters:
            s += (ord(c) - 96)
        if s > 26:
            s = int(s % 26)
            if s == 0:
                return 'z'
        return chr(s + 96)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        l = [i for i in input('>>> Enter alphabets to sum with comma-separated: ').split(',')]
        print(add_letters(l))
    else:
        sys.exit(1)
