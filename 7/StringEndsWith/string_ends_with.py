import sys


def solution(string, ending):
    if ending == '':
        return True
    w = string.split(ending)
    return (w[-1] == '')


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(solution(string=sys.argv[1], ending=sys.argv[2]))
    else:
        sys.exit(1)
