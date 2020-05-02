import sys


def int_diff(arr, n):
    ans = []
    arr = sorted(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] - arr[i] == n:
                ans.append((arr[i], arr[j]))
    return len(ans)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = [int(i) for i in input('>>> Enter numbers with comma-separated: ').split(',')]
        if inp is not []:
            j = int(input('>>> Enter diffs to find: '))
            print(int_diff(arr=inp, n=j))
        else:
            print('Err, please enter some numbers.')
            sys.exit(1)
    else:
        sys.exit(1)
