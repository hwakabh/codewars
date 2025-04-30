import sys


def get_sum_of_digits(num):
    return sum(int(n) for n in str(num))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(get_sum_of_digits(num=int(sys.argv[1])))
    else:
        sys.exit(1)
