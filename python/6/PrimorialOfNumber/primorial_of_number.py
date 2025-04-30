import sys


def num_primorial(n):
    pn = [2]
    i = 2
    while True:
        i += 1
        if len(pn) >= n:
            break
        else:
            is_prime = True
            for p in pn:
                if i % p == 0:
                    is_prime = False
                    break
            if is_prime:
                pn.append(i)

    ans = 1
    for a in pn[:n]:
        ans *= a
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(num_primorial(n=int(sys.argv[1])))
    else:
        sys.exit(1)
