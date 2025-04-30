import sys


def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    elif 0 <= m < 60:
        return 'F'


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(get_grade(s1=int(sys.argv[1]), s2=int(sys.argv[2]), s3=int(sys.argv[3])))
    else:
        sys.exit(1)
