import sys


def two_sum(numbers, target):
    for i, n in enumerate(numbers):
        for j in range(len(numbers)):
            if j == 0:
                pass
            else:
                if n + numbers[j] == target:
                    return [i, j]



if __name__ == "__main__":
    if len(sys.argv) == 1:
        n = [int(i) for i in input('>>> Enter numbers for candidates with comma-separated: ').split(',')]
        t = int(input('>>> Enter the target numbers: '))
        print(two_sum(numbers=n, target=t))
    else:
        sys.exit(1)
