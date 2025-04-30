import sys


def tickets(people):
  q = 0
  h = 0
  for p in people:
      if p == 25:
          q += 1
      elif p == 50:
          q -= 1
          h += 1
      elif (p == 100) and (h > 0):
          q -= 1
          h -= 1
      elif (p == 100) and (h == 0):
          q -= 3
      if (q < 0) or (h < 0):
          return 'NO'
  return 'YES'


if __name__ == "__main__":
    if len(sys.argv) == 1:
        p = [ int(c) for c in input('Enter the order for clerk with comma-splitted: ').split(',')]
        print(tickets(people=p))
    else:
        sys.exit(1)