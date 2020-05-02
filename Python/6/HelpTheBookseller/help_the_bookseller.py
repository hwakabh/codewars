import sys


def stock_list(listOfArt, listOfCat):
    s = ''
    for c in listOfCat:
        p = 0
        for a in listOfArt:
            if c == a[0]:
                p += int(a.split(' ')[1])
        s += '({0} : {1}) - '.format(c, p)
    if s.count(': 0') == len(listOfCat):
        return ''
    else:
        return s[:-3]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        pass
    else:
        sys.exit(1)
