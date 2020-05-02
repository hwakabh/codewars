import sys


def make_change(amount):
    c = {}
    k = [{'H': 50}, {'Q': 25}, {'D': 10}, {'N': 5}, {'P': 1}]
    for t in k:
        r = 0
        while amount >= sum(t.values()):
            amount -= sum(t.values())
            r += 1
        c[list(t.keys())[0]] = r
    return {k: v for k, v in c.items() if not v == 0}


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(make_change(amount=int(sys.argv[1])))
    else:
        sys.exit(1)
