import sys


def golf_score_calculator(par_string, score_string):
    s = 0
    for i in range(18):
        s += (int(score_string[i]) - int(par_string[i]))
    return s


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(golf_score_calculator(
            par_string=sys.argv[1],
            score_string=sys.argv[2]
        ))
    else:
        sys.exit(1)
