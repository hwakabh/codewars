import sys


def thirt(n):
    dv = [1, 10, 9, 12, 3, 4]

    def get_divisor_sum(x):
        s = 0
        for i, t in enumerate(reversed(str(x))):
            s += (int(t) * dv[i % 6])
        return s

    ans = get_divisor_sum(x=n)
    while True:
        ans = get_divisor_sum(x=ans)
        if ans == get_divisor_sum(ans):
            break
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(thirt(n=int(sys.argv[1])))
    else:
        sys.exit(1)
