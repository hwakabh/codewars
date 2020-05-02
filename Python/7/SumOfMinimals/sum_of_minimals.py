import sys


def sum_of_minimals(numbers):
    s = 0
    for arr in numbers:
        s += sorted(arr)[0]
    return s


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('>>> Enter the arrays with comma and brackets separated: ')
        print('>>> \t e.g. [1,3,5,7,9],[2,4,6,8]')
        user_inputs = input('>>> ')
        arrays = [[int(i) for i in a.replace('[', '').replace(']', '').split(',')] for a in user_inputs.split('],[')]
        print(sum_of_minimals(numbers=arrays))
    else:
        sys.exit(1)
