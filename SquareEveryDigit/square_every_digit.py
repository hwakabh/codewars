import sys


def square_digits(num):
    if isinstance(num, int):
        num = str(num)
    ans = ''
    for n in num:
        ans += str(int(n) * int(n))
    return int(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(square_digits(num=sys.argv[1]))
    else:
        sys.exit(1)