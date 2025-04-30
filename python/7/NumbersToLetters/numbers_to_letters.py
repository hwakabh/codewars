import sys


def switcher(arr):
    w = []
    for d in arr:
        if 1 <= int(d) <= 26:
            w.append(chr(123 - int(d)))
        elif int(d) == 27:
            w.append('!')
        elif int(d) == 28:
            w.append('?')
        elif int(d) == 29:
            w.append(' ')
    return ''.join(w)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter numbers to switch as letters with comma-separeted: ').split(',')
        print(switcher(arr=inp))
    else:
        sys.exit(1)
