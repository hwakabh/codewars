import sys


def nth_char(words):
    ans = ''
    for i, w in enumerate(words):
        ans += w[i]
    return ans


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(nth_char(words=sys.argv[1:]))
    else:
        sys.exit(1)
