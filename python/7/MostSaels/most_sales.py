import sys


def top3(products, amounts, prices):
    revenues = [amounts[i] * prices[i] for i in range(len(products))]
    index = sorted(
        range(len(revenues)),
        key= lambda j : revenues[j],
        reverse=True
        )
    return [products[k] for k in index][:3]


if __name__ == "__main__":
    if len(sys.argv) == 1:
        products = input('Enter products with comma-separed: ').split(',')
        amounts = input('Enter amounts with comma-separed: ').split(',')
        prices = input('Enter prices with comma-separed: ').split(',')
        print(top3(products=products, amounts=amounts, prices=prices))
    else:
        sys.exit(1)
