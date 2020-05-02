import sys


def correct_polish_letters(st):
    matches = {
        'ą': 'a',
        'ć': 'c',
        'ę': 'e',
        'ł': 'l',
        'ń': 'n',
        'ó': 'o',
        'ś': 's',
        'ź': 'z',
        'ż': 'z'
    }
    return ''.join(matches[c] if c in matches.keys() else c for c in st)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        string = ' '.join(sys.argv[1:])
        print(correct_polish_letters(st=string))
    else:
        sys.exit(1)
