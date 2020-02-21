import sys


def reverse_seq(n):
    return sorted([i + 1 for i in range(n)], reverse=True)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(reverse_seq(n=int(sys.argv[1])))
    else:
        sys.exit(1)