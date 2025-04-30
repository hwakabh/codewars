import sys


def cyclops(n):
    strn = bin(n).replace('0b', '')
    if strn.count('0') != 1:
        return False
    else:
        m = n.bit_length() // 2 + 1
        if len(strn[m:]) != len(strn[0:m-1]):
            return False
        else:
            if ('0' not in strn[m:]) and ('0' not in strn[0:m-1]):
                return True
            else:
                return False


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(cyclops(n=int(sys.argv[1])))
    else:
        sys.exit(1)
