import sys


def hero(bullets, dragons):
    return (bullets / dragons >= 2)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(hero(bullets=int(sys.argv[1]), dragons=int(sys.argv[2])))
    else:
        sys.exit(1)
