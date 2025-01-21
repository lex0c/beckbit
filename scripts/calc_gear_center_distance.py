import argparse


def calculate_center_distance(module, teeth_gear1, teeth_gear2):
    """
    Calculates the center distance between two gears.

    :param module: Module of the gears (m)
    :param teeth_gear1: Number of teeth on the driving gear (z1)
    :param teeth_gear2: Number of teeth on the driven gear (z2)
    :return: Center distance (dc)
    """

    diameter1 = module * teeth_gear1  # Diameter of the driving gear
    diameter2 = module * teeth_gear2  # Diameter of the driven gear

    center_distance = (diameter1 + diameter2) / 2

    return center_distance


def main():
    parser = argparse.ArgumentParser(description="Calculate the center distance between two gears.")
    parser.add_argument("-m", "--module", type=float, required=True, help="Module of the gears")
    parser.add_argument("-z1", "--teeth_gear1", type=int, required=True, help="Number of teeth on the driving gear")
    parser.add_argument("-z2", "--teeth_gear2", type=int, required=True, help="Number of teeth on the driven gear")

    args = parser.parse_args()

    center_distance = calculate_center_distance(args.module, args.teeth_gear1, args.teeth_gear2)

    print(f"The center distance between the gears is: {center_distance:.2f}mm")


if __name__ == "__main__":
    main()

