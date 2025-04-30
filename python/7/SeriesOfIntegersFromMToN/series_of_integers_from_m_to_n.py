import sys


def generate_integers(m, n):
    return [i for i in range(m, n + 1)]


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(generate_integers(m=int(sys.argv[1]), n=int(sys.argv[2])))
    else:
        sys.exit(1)
