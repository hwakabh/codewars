import sys


def better_than_average(class_points, your_points):
    avg = sum([int(i) for i in class_points]) / len(class_points)
    return your_points > avg


if __name__ == "__main__":
    if len(sys.argv) == 1:
        nums = [int(x) for x in input('>>> Enter your class points with comma-separated: ').split(',')]
        p = int(input('>>> Enter your score: '))
        print(better_than_average(class_points=nums, your_points=p))
    else:
        sys.exit(1)
