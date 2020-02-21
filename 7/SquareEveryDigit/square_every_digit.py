import sys


def square_digits(num):
    ans = ''
    for n in str(num):
        ans += str(int(n) ** 2)
    return int(ans)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(square_digits(num=int(sys.argv[1])))
    else:
        sys.exit(1)