import sys


def next_happy_year(year):
    year += 1
    while len(set(str(year))) != len(str(year)):
        year += 1
    return year


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(next_happy_year(year=int(sys.argv[1])))
    else:
        sys.exit(1)
