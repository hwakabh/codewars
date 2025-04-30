import sys


def number_of_occurrence(element, sample):
    return sample.count(element)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        sample = input('>>> Enter your array for check with comma-separated: ')
        print(sample)
        element = input('>>> Enter the element to find: ')
        print(number_of_occurrence(element=element, sample=sample))
    else:
        sys.exit(1)