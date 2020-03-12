import sys


def remove_duplicate(arr):
    l = []
    for d in arr:
        if d not in l:
            l.append(d)
    return l


if __name__ == "__main__":
    if len(sys.argv) == 1:
        d = [w for w in input('>>> Enter some data for removing duplicates with comma separated: ').split(',')]
        data = []
        for v in d:
            data.append({'data': {'id': v}})
        print(remove_duplicate(arr=data))
    else:
        sys.exit(1)
