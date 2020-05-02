import sys

def spin_words(sentence):
    s = sentence.split(' ')
    for i, word in enumerate(s):
        if len(word) >= 5:
            s[i] = word[::-1]
    return ' '.join(s)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(1)
    else:
        str_sentence = ' '.join(sys.argv[1:])
        print(spin_words(sentence=str_sentence))
