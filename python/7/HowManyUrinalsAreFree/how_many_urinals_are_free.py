import sys


def get_free_urinals(urinals):
    if urinals.count("11") >= 1:
        return -1
    
    u = "0" + urinals + "0"
    c = 0
    while "000" in u:    
        u = u.replace("000", "010", 1)
        c += 1
    return c


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(get_free_urinals(urinals=sys.argv[1]))
    else:
        sys.exit(1)
