import sys


def square_sum(numbers):
    return sum([n ** 2 for n in numbers])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nums = [int(e) for e in input('>>> Enter the numbers with comma-separeted: ').split(',')]
        print(square_sum(numbers=nums))
    else:
        sys.exit(1)