import sys


def duplicate_count(text):
    count = 0
    text = text.lower()
    arr = []
    for i, c in enumerate(text.lower()):
        if c in text[i+1:]:
            if c not in arr:
                count += 1
                arr.append(c)
    return count


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(duplicate_count(text=sys.argv[1]))
    else:
        sys.exit(1)
