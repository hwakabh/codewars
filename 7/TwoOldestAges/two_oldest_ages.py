import sys


def two_oldest_ages(ages):
    return sorted(ages)[len(ages)-2:len(ages)]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        a = [int(c) for c in input('>>> Enter ages to check with comma-separated: ').split(',')]
        print(two_oldest_ages(ages=a))
    else:
        sys.exit(1)
