import sys


def absent_vowel(x):
    vowels = ['A', 'E', 'I', 'O', 'U']
    for i, v in enumerate(vowels):
        if v.lower() not in x.lower():
            return i


if __name__ == "__main__":
    if len(sys.argv) == 1:
        string = input('>>> Enter some strings: ')
        print(absent_vowel(x=string))
    else:
        sys.exit(1)
