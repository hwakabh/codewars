import sys


def parts_sums(ls):
    arr = [sum(ls[i::]) for i in range(len(ls))]
    arr.append(0)
    return arr


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(i) for i in input('>>> Enter numbers with comma-separated: ').split(',')]
        print(parts_sums(ls=inp))
    else:
        sys.exit(1)
