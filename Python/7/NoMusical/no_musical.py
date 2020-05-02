import sys


def no_musical(start_class, end_class, musical_performed_every, enrolment_duration):
    if musical_performed_every == 0:
        return end_class - start_class + 1
    else:
        if start_class == end_class:
            return 0
        c = 0
        musicals = range(start_class, end_class + 1, musical_performed_every)
        for i in range(start_class, end_class):
            view = [y for y in range(i, i+enrolment_duration) if y in musicals]
            if len(view) == 0:
                c += 1
        return c


if __name__ == "__main__":
    if len(sys.argv) == 1:
        lst = [int(n) for n in input('>>> Enter start_class,end_class,musical_performed_every,enrolment_duration: ').split(',')]
        print(no_musical(start_class=lst[0], end_class=lst[1], musical_performed_every=lst[2], enrolment_duration=lst[3]))
    else:
        sys.exit(1)
