import sys


def sort_number(a): 
    if len(a) == 1:
        if a[0] == 1:
            return [2]
        else:
            return [1]
    else:
        arr = sorted(a)
        if set(a) == {1}:
            arr.pop(len(arr) - 1)
            arr.append(2)
        else:
            arr.insert(0, 1)
            arr.pop(len(arr) - 1)
        return arr


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(c) for c in input('>>> Enter numbers to sort with comma-separated: ').split(',')]
        print(sort_number(a=inp))
    else:
        sys.exit(1)
