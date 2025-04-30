import sys


def solution(s):
    w = ''
    for c in s:
        if not c.islower():
            w += ' {}'.format(c)
        else:
            w += c
    return w


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(solution(s=sys.argv[1]))
    else:
        sys.exit(1)
