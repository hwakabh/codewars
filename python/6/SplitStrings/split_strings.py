import sys
from itertools import zip_longest

def solution(s):
    ans = []
    evens = [c for i, c in enumerate(s) if i % 2 ==0]
    odds = [c for i, c in enumerate(s) if i % 2 !=0]

    for e, o in zip_longest(evens, odds, fillvalue='_'):
        ans.append(e + o)

    return ans


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(solution(s=sys.argv[1]))
    else:
        sys.exit(1)
