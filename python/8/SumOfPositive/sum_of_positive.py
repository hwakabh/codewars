import sys


def positive_sum(arr):
    return sum([m for m in arr if m > 0])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nums = [int(n) for n in input('>>> Enter numbers to add with comma-separated: ').split()]
        print(positive_sum(arr=nums))
    else:
        sys.exit(1)
