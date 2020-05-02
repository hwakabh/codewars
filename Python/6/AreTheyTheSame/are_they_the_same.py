import sys


def comp(array1, array2):
    if (array1 == None) or (array2 == None):
        return False
    else:
      s = sorted([i ** 2 for i in array1])
      return (s == sorted(array2))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        a1 = [int(i) for i in input('>>> Enter first arrays with comma-separated: ').split(',')]
        a2 = [int(j) for j in input('>>> Enter second arrays with comma-separated: ').split(',')]
        print(comp(array1=a1, array2=a2))
    else:
        sys.exit(1)
