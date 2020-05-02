import sys


def is_vowel(s):
    return (s.lower() in ['a', 'i', 'u', 'e', 'o'])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(is_vowel(s=sys.argv[1]))
    else:
        sys.exit(1)
