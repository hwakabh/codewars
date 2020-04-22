from unittest import TestCase
from unittest import main

from pokemon_damage_calculator import calculate_damage


class TestPokemonDamageCalculator(TestCase):
    def test_calculate_damage(self):
        ptr = [
            ('fire', 'water', 100, 100, 25),
            ('grass', 'water', 100, 100, 100),
            ('electric', 'fire', 100, 100, 50),
            ('grass', 'electric', 57, 19, 150),
            ('grass', 'water', 40, 40, 100),
            ('grass', 'fire', 35, 5, 175),
            ('fire', 'electric', 10, 2, 250),
        ]
        for t, o, atk, dfs, exp in ptr:
            with self.subTest(t=t, o=o, atk=atk, dfs=dfs, exp=exp):
                self.assertEqual(calculate_damage(your_type=t, opponent_type=o, attack=atk, defense=dfs), exp)


if __name__ == '__main__':
    main(verbosity=2)
