import sys


def calculate_damage(your_type, opponent_type, attack, defense):
    e = 1
    if your_type == opponent_type:
        e = 0.5

    if your_type == 'fire':
        if opponent_type == 'grass':
            e = 2
        elif opponent_type == 'water':
            e = 0.5
    elif your_type == 'water':
        if (opponent_type == 'grass') or (opponent_type == 'electric'):
            e = 0.5
        elif opponent_type == 'fire':
            e = 2
    elif your_type == 'grass':
        if opponent_type == 'fire':
            e = 0.5
        elif opponent_type == 'water':
            e = 2
    elif your_type == 'electric':
        if opponent_type == 'water':
            e = 2
    return 50 * (attack / defense) * e


if __name__ == "__main__":
    if len(sys.argv) == 1:
        types = input('>>> Enter types of your/opponent with comma-separated [fire/water/electric/grass]: ').split(',')
        if len(types) != 2:
            sys.exit(1)
        else:
            powers = input('>>> Enter powers of your-attack/opponent-defense with comma-separated: ').split(',')
            if len(powers) != 2:
                sys.exit(1)
            else:
                print(calculate_damage(your_type=types[0], opponent_type=types[1], attack=int(powers[0]), defense=int(powers[1])))
    else:
        sys.exit(1)
