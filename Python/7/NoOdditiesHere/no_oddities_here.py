import sys


def no_odds(values):
    return [j for j in values if j % 2 == 0]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        n = [int(i) for i in input('>>> Enter some numbers with comma-separated: ').split(',')]
        print(no_odds(values=n))
    else:
        sys.exit(1)
