import sys

def goals(laLiga, copaDelRey, championsLeague):
    return (laLiga + copaDelRey + championsLeague)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        goal_total = [int(g) for g in input('>>> Enter Messi\'s goal total with comma-separated: ').split(',')]
        print(
            goals(
                laLiga=goal_total[0],
                copaDelRey=goal_total[1],
                championsLeague=goal_total[2]
            )
        )
    else:
        sys.exit(1)
