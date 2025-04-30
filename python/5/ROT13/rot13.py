import sys


def rot13(message):
    cipher = []
    for c in message:
        if c.isalpha():
            k = ord(c) + 13
            if c.isupper():
                if 90 < k <= 122:
                    k = k - 91 + 65
            else:
                if 122 < k:
                    k = k - 123 + 97
            cipher.append(chr(k))
        else:
            cipher.append(c)
    return ''.join(cipher)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Please enter your message to encrypt: ')
        print(rot13(message=inp))
    else:
        print('Err, please run without any arguments.')
        sys.exit(1)
