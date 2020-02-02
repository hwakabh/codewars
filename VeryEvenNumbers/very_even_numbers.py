import sys


def is_very_even_number(n):
    while True:
        sum_digit = 0
        for d in str(n):
            sum_digit += int(d)
        if sum_digit >= 10:
            n = sum_digit
        else:
            break
    return (sum_digit % 2 == 0)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(is_very_even_number(n=int(sys.argv[1])))
    else:
        sys.exit(1)