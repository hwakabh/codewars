import sys

def sum_triangular_numbers(n):
    if n <= 0:
        return 0
    else:
        t = [int((i + 1) * (i + 2) / 2) for i in range(n)]
        return sum(t)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(sum_triangular_numbers(n=int(sys.argv[1])))
    else:
        sys.exit(1)
