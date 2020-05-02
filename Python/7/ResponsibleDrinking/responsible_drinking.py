import sys


def hydrate(drink_string):
    nums = []
    for w in drink_string.split():
        if len(w) == 1:
            nums.append(int(w))
    if sum(nums) == 1:
        return '1 glass of water'
    else:
        return '{} glasses of water'.format(sum(nums))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        order = input('>>> Enter your drink order: ')
        print(hydrate(drink_string=order))
    else:
        sys.exit(1)
