import sys


def is_uppercase(inp):
    for c in inp:
        if c.islower():
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) == 1:
        string = input('>>> Enter strings for checking: ')
        print(is_uppercase(inp=string))
    else:
        sys.exit(1)
