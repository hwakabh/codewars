import sys


def duplicate_count(text):
    t = text.lower()
    d = []
    for i, c in enumerate(t):
        if c in t[i+1:]:
            if c not in d:
                d.append(c)
    return len(d)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(duplicate_count(text=sys.argv[1]))
    else:
        sys.exit(1)
