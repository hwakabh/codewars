import sys


def sum_two_smallest_numbers(numbers):
    r_numbers = sorted(numbers)
    return r_numbers[0] + r_numbers[1]


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        inputs = []
        for n in sys.argv[1:]:
            inputs.append(int(n))
        print(sum_two_smallest_numbers(numbers=inputs))
