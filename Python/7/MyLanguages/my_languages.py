import sys


def my_languages(results):
    # Sort dict by its values
    r = sorted(results.items(), key=lambda x: x[1], reverse=True)
    # Get key/value of tuples
    l = [i[0] for i in r if i[1] >= 60]
    return l


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('>>> Enter your results for each languages with comma-separated: ')
        print('Examples: \'Java\':10,\'Ruby\':80,\'Python\':65')
        r = input('>>> ')
        print(my_languages(results=r))
    else:
        sys.exit(1)
