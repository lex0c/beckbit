import argparse
import math


def calculate_belt_length(d1, d2, c):
    """Calculates the belt length."""
    length = (2 * c) + (math.pi / 2) * (d1 + d2) + ((d2 - d1) ** 2) / (4 * c)
    return length


def main():
    parser = argparse.ArgumentParser(description="Calculate the belt length.")
    parser.add_argument("-d1", type=float, required=True, help="Diameter of the driving pulley (D1) in millimeters.")
    parser.add_argument("-d2", type=float, required=True, help="Diameter of the driven pulley (D2) in millimeters.")
    parser.add_argument("-c", type=float, required=True, help="Distance between the centers of the pulleys (C) in millimeters.")
    parser.add_argument("-p", type=float, required=False, default=None, help="Pitch of the belt (optional) in millimeters, if toothed.")

    args = parser.parse_args()

    belt_length = calculate_belt_length(args.d1, args.d2, args.c)

    print(f"Calculated belt length: {belt_length:.2f}mm")

    # If the pitch is provided, calculate the number of teeth
    if args.p:
        num_teeth = belt_length / args.p
        print(f"Approximate number of teeth (rounded): {math.ceil(num_teeth)}")


if __name__ == "__main__":
    main()

