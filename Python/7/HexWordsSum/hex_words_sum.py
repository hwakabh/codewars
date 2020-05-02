import sys


def hex_word_sum(string):
    keys = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 's': 5, 'o': 0}
    words = string.split()
    sums = 0
    for w in words:
      subtotal = 0
      for i, c in enumerate(w[::-1].lower()):
          if c in keys:
              subtotal += keys[c] * (16 ** i) 
          else:
              subtotal = 0
              break
      sums += subtotal
    return sums

if __name__ == "__main__":
    if len(sys.argv) != 1:
        print(hex_word_sum(string=' '.join(sys.argv[1:])))
    else:
        sys.exit(1)