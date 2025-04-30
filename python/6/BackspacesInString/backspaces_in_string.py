import sys


def clean_string(s):
    stdout = []
    for c in s:
        if c == '#':
            if len(stdout) != 0:
                stdout.pop()
            else:
                pass
        else:
            stdout.append(c)
    return ''.join(stdout)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(clean_string(s=sys.argv[1]))
    else:
        sys.exit(1)
