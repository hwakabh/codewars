import sys


def digital_root(n):
    while True:
        nums = [int(i) for i in str(n)]
        if sum(nums) < 10:
            return sum(nums)
        else:
            n = sum(nums)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(digital_root(n=int(sys.argv[1])))
    else:
        sys.exit(1)
