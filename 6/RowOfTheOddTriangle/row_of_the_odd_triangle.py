import sys


def odd_row(n):
    f = n ** 2 - (n - 1)
    e = (n + 1) ** 2 - (n + 1 - 1)
    # Sum of odd_row is n ** 3
    # -> middle_of_row = n^2
    #              1                : n=1, S=1
    #           3 (4) 5             : n=2, S=(3+5)+4=(4*2)+4
    #        7     9    11          : n=3, S=(7+11)+9=(9*2)+9
    #    13   15 (16) 17   19       : n=4, S=(13+19+15+17)+16=(16*2+16*2)+16
    # 21    23    25    27    29    : n=5, S=(21+29+23+27)+25=(25*2+25*2)+25
    return list(range(f, e, 2))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(odd_row(n=int(sys.argv[1])))
    else:
        sys.exit(1)
