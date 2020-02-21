import sys


def count_letters_and_digits(s):
    counter = 0
    for c in s:
        if (c.isalpha() or c.isdigit()):
            counter += 1
    return counter


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(count_letters_and_digits(s=sys.argv[1]))
    else:
        sys.exit(1)