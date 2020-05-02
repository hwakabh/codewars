import sys


def string_letter_count(s):
    s = sorted(s.lower())
    result = ''

    l = list(set(s))
    t = ''.join(s)
    for c in sorted(l):
        if c.isalpha():
            r = '{0}{1}'.format(t.count(c), c)
            result += r
    return result


if __name__ == "__main__":
    if len(sys.argv) == 1:
        string = input('>>> Enter string to count up: ')
        print(string_letter_count(s=string))
    else:
        sys.exit(1)
