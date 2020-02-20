import sys


def am_I_afraid(day, num):
    if day == 'Monday':
      return num==12
    elif day == 'Tuesday':
      return num > 95
    elif day == 'Wednesday':
      return num == 34
    elif day == 'Thursday':
      return num == 0
    elif day == 'Friday':
      return num % 2 == 0
    elif day == 'Saturday':
      return num == 56
    elif day == 'Sunday':
      return num == 666 or num == -666


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(am_I_afraid(day=sys.argv[1], num=int(sys.argv[2])))
    else:
        sys.exit(1)
