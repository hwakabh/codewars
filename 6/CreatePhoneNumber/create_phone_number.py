import sys


def create_phone_number(n):
    s = ''.join([str(c) for c in n])
    return '({0}) {1}-{2}'.format(s[:3], s[3:6], s[6:])


if __name__ == "__main__":
    num_array = [int(n) for n in input('Enter numbers with comma-splited : ').split(',')]
    if len(num_array) == 9:
        print(create_phone_number(n=num_array))
    else:
        sys.exit(1)