import sys


def mouth_size(animal):
    if animal.lower() == 'alligator':
        return 'small'
    else:
        return 'wide'


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(mouth_size(animal=sys.argv[1]))
    else:
        sys.exit(1)
