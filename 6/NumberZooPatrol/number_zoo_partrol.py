import sys


def find_missing_number(numbers):
    for n in range(1, len(numbers) + 1):
        if n not in numbers:
            return n
    return max(numbers) + 1


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nums = [int(n) for n in input('>>> Enter numbers to find comma-separated: ').split(',')]
        print(find_missing_number(numbers=nums))
    else:
        sys.exit(1)
