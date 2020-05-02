import sys


def to_alternating_case(string):
    case = ''
    for c in string:
        if c.islower():
            case += c.upper()
        elif c.isupper():
            case += c.lower()
        else:
            case += c
    return case


if __name__ == "__main__":
    if len(sys.argv) == 1:
        s = input('>>> Enter some strings to alternate')
        print(to_alternating_case(string=s))
    else:
        sys.exit(1)
