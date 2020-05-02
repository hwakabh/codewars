import sys


def dashtize(num):
    if num is None:
        return 'None'

    n = str(num.__abs__())
    number = ''.join(['-{}-'.format(c) if int(c) % 2 != 0 else c for c in n]).replace('--', '-')
    if number[0] == '-' and number[len(number) - 1] == '-':
        return number[1:len(number)-1]
    elif number[0] == '-':
        return number[1:]
    elif number[len(number) - 1] == '-':
        return number[0:len(number)-1]
    else:
        return number


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(dashtize(num=int(sys.argv[1])))
    else:
        sys.exit(1)
