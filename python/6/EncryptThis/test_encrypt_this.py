from unittest import TestCase
from unittest import main

from .encrypt_this import encrypt_this


class TestEncryptThis(TestCase):
    def test_encrypt_this(self):
        ptr = [
            ('', ''),
            ('A wise old owl lived in an oak', '65 119esi 111dl 111lw 108dvei 105n 97n 111ka'),
            ('The more he saw the less he spoke', '84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp'),
            ('The less he spoke the more he heard', '84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare'),
            ('Why can we not all be like that wise old bird', '87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri'),
            ('Thank you Piotr for all your help', '84kanh 121uo 80roti 102ro 97ll 121ruo 104ple'),
        ]
        for inp, exp in ptr:
            with self.subTest(inp=inp, exp=exp):
                self.assertEqual(encrypt_this(text=inp), exp)


if __name__ == '__main__':
    main(verbosity=2)
