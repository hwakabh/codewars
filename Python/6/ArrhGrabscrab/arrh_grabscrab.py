import sys


def grabscrab(word, possible_words):
    words = [''.join(sorted(w)) for w in possible_words]
    ans = []
    for i, w in enumerate(words):
        if w == ''.join(sorted(word)):
            ans.append(possible_words[i])
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 2:
        words = input('>>> Enter the possible words with comma-separated: ')
        print(grabscrab(word=sys.argv[1], possible_words=words))
    else:
        sys.exit(1)
