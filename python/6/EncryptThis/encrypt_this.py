import sys


def encrypt_this(text):
    w = text.split(' ')
    ans = []

    for i in w:
        x = ''
        if len(i) >= 3:
            x = str(ord(i[0])) + i[len(i)-1:] + i[2:len(i)-1] + i[1]
        elif len(i) == 3:
            x = str(ord(i[0])) + i[len(i)-1:] + i[1]
        elif len(i) == 2:
            x = str(ord(i[0])) + i[1]
        elif len(i) == 1:
            x = str(ord(i[0]))
        ans.append(x)
    
    return ' '.join(ans)


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        inp = ' '.join(sys.argv[1:])
        print(encrypt_this(text=inp))
    else:
      sys.exit(1)
