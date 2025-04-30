import sys


def capital(capitals):
    ans = []
    for c in capitals:
        k = c.get('state')
        if k is None:
            k = c.get('country')
        ans.append('The capital of {0} is {1}'.format(k, c.get('capital')))
    return ans


if __name__ == "__main__":
    if len(sys.argv) == 1:
        cap = input('>>> Enter the capital: ')
        state = input('>>> Enter the state/country name: ')
        d = {'state': state, 'capital': cap}
        print(capital(capitals=d))
    else:
        sys.exit(1)
