import sys


def disemvowel(string):
    vowels = ['a', 'A', 'o', 'O', 'i', 'I', 'u', 'U', 'e', 'E']
    for v in vowels:
        if v in string:
            string = string.replace(v, '')
    return string


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter sentence to remove vowels: ')
        print(disemvowel(string=inp))
    else:
        sys.exit(1)
