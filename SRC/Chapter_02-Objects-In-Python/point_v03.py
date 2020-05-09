import math


class Point:
    "Represents a point in two-dimensinal geometric coordinates"

    def __init__(self, x=0, y=0):
        """Initialize the postion of a new point. The x and y coordinate
        can be specified. If they are not, the point defaults to the origin. """
        self.move(x, y)

    # Move method
    def move(self, x, y):
        """Move the point to a new locationin 2-d space."""
        self.x = x
        self.y = y

    # self is a manditory name.
    def reset(self):
        """Reset the point back to the geometric origin: 0, 0"""
        self.move(0, 0)

    # Calculate distance
    def calculate_distance(self, other):
        """Calculate the distance from this point to a second point passed as a parameter.
            This function uses the Pythagorean Theorem to calculate the distance between the two points.
            The difference is returned as a flot."""
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))


if __name__ == "__main__":
    help(Point)
