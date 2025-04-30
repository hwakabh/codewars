import sys
from math import ceil


def calculate_tip(amount, rating):
    items = {
        'terrible': 0,
        'poor': 0.05,
        'good': 0.1,
        'great': 0.15,
        'excellent': 0.2
    }
    if rating.lower() in items.keys():
        return ceil(amount * items[rating.lower()])
    else:
        return 'Rating not recognised'


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(calculate_tip(amount=int(sys.argv[1]), rating=sys.argv[2]))
    else:
        sys.exit(1)
