import sys


def monkey_count(n):
    return [i + 1 for i in range(n)]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(monkey_count(n=int(sys.argv[1])))
    else:
        sys.exit(1)
