import sys


def get_planet_name(id):
    planets = {
        1: 'Mercury',
        2: 'Venus',
        3: 'Earth',
        4: 'Mars',
        5: 'Jupiter',
        6: 'Saturn',
        7: 'Uranus',  
        8: 'Neptune'
    }
    return planets.get(id, None)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(get_planet_name(id=int(sys.argv[1])))
    else:
        sys.exit(1)
