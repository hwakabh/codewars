import sys


def getVolumeOfCuboid(length, width, height):
    return length * width * height


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(getVolumeOfCuboid(
            length=sys.argv[1],
            width=sys.argv[2],
            height=sys.argv[3]
            )
        )
    else:
        sys.exit(1)
