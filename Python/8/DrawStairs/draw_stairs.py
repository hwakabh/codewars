import sys


def draw_stairs(n):
    string = ''
    for i in range(n):
        string += '{0}{1}\n'.format(' ' * i, 'I')
    return string.rstrip()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(draw_stairs(n=int(sys.argv[1])))
    else:
        sys.exit(1)
