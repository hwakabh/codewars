import sys


def points(games):
    p = 0
    for m in games:
        if int(m.split(':')[0]) > int(m.split(':')[1]):
            p += 3
        elif int(m.split(':')[0]) == int(m.split(':')[1]):
            p += 1
        else:
            pass
    return p


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('>>> Enter the results of games with comma-separated: ')
        print('Format exmaples: 3:1,4:1,5:1 ...')
        g = input('>>>> ')
        print(points(games=g))
    else:
        sys.exit(1)
