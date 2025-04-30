import sys


def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (distance_to_pump <= mpg * fuel_left)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        print(zero_fuel(
            distance_to_pump=int(sys.argv[1]),
            mpg=int(sys.argv[2]),
            fuel_left=int(sys.argv[3])
            ))
    else:
        sys.exit(1)
