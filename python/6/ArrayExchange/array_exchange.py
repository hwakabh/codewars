import sys


def exchange_with(a, b):
    invert_a = list(reversed(a))
    invert_b = list(reversed(b))
    a.clear()
    b.clear()
    for i in invert_b:
        a.append(i)
    for j in invert_a:
        b.append(j)
    # As solutions, it should return multiple array values
    # -> return a, b
    return (a, b)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        array1 = input('>>> Enter the first array with comma-separated: ').split(',')
        array2 = input('>>> Enter the second array with comma-separated: ').split(',')
        print(exchange_with(a=array1, b=array2))
    else:
        sys.exit(1)
