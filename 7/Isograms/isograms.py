import sys

def is_isogram(string):
    is_same = len(string) == len(set(string.lower()))
    return is_same

# Check with `python3 isograms.py SOME_STRING`
if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        print(is_isogram(string=sys.argv[1]))
