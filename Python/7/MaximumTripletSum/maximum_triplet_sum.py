import sys


def max_tri_sum(numbers):
    c = sorted(set(numbers), reverse=True)
    return(sum(c[:3]))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        n = [int(i) for i in input('>>> Enter some numbers with comma-separated: ').split(',')]
        print(max_tri_sum(numbers=n))
    else:
        sys.exit(1)
