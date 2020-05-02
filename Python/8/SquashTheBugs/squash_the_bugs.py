import sys


def find_longest(string):
    ### Fix-Me type problem-set
    # spl = str.split(" ")
    # longest = 0
    # i=0
    # while (i > spl.length):
    # if (spl(i).length > longest): longest = spl[i].length
    # return longest
    spl = string.split(" ")
    return max([len(n) for n in spl])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        p = input('>>> Enter the sentence to find longest word: ')
        print(find_longest(string=p))
    else:
        sys.exit(1)
