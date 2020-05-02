import sys


def greatest_product(n):
    arr = []
    for i in range(len(n)):
        d = n[i:i+5]
        if len(d) == 5:
            subtotal = 1
            for j in d:
                subtotal *= int(j)
            arr.append(subtotal)
    return max(arr)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(greatest_product(n=sys.argv[1]))
    else:
        print('Err: Argument missing, please provide an arguments to find largest product.')
        sys.exit(1)
