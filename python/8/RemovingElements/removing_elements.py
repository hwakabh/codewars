import sys


def remove_every_other(my_list):
    return [my_list[i] for i in range(len(my_list)) if i % 2 != 1]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        inp = input('>>> Enter elements for your list with comma-separated: ').split(',')
        print(remove_every_other(my_list=inp))
    else:
        sys.exit(1)
