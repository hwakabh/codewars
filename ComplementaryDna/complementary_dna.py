import sys


def DNA_stand(dna):
    ordered_dna = []
    for c in dna:
        if c == 'A':
            ordered_dna.append('T')
        elif c == 'T':
            ordered_dna.append('A')
        elif c == 'C':
            ordered_dna.append('G')
        elif c == 'G':
            ordered_dna.append('C')
        else:
            pass
    return ''.join(ordered_dna)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(DNA_stand(dna=sys.argv[1]))
    else:
        sys.exit(1)