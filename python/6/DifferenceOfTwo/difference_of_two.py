import sys


def twos_differnece(lst):
    lst = sorted(lst)
    d = []
    for i in lst:
        p = [i]
        if i + 2 in lst:
            p.append(i + 2)
            d.append(tuple(p))
    return d


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nums = [int(n) for n in input('>>> Enter numbers to find diffs of 2 with comma-separated: ').split(',')]
        print(twos_differnece(lst=nums))
    else:
        sys.exit(1)
