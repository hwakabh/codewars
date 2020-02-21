import sys

def duplicate_encode(word):
    encode_word = ['(' if word.lower().count(c) == 1 else ')' for c in word.lower()]
    return ''.join(encode_word)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(duplicate_encode(word=sys.argv[1]))
    else:
        sys.exit(1)