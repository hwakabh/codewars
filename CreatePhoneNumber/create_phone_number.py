import sys


def create_phone_number(n):
    # TODO: Refactor with for-loop
    return '({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}'.format(n[0], n[1], n[2], n[3], n[4], n[5], n[6], n[7], n[8], n[9])


if __name__ == "__main__":
    num_array = [int(n) for n in input('Enter numbers with comma-splited : ').split(',')]
    if len(num_array) == 9:
        print(create_phone_number(n=num_array))
    else:
        sys.exit(1)