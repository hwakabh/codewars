import sys


def DNA_stand(dna):
    pairs = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    return ''.join([pairs[c] for c in dna])


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(DNA_stand(dna=sys.argv[1]))
    else:
        sys.exit(1)