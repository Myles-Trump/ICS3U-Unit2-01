#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program lets the user calculate the perimeter and area
#  of a circle by entering in the radius

import math


def main():
    # this function lets the user calculate the perimeter and area
    #  of a circle by entering in the radius

    # input
    radius = int(input("Enter the radius (mm): "))

    # process
    perimeter = math.pi * 2 * radius
    area = math.pi * radius ** 2

    # output
    print("\nThe perimeter is {0} mm and the area is {1} mm²."
          .format(perimeter, area))
    print("\nDone.")


if __name__ == "__main__":
    main()
