import math


class Point:
    # passing default aguments to we never have empty point attributes.
    def __init__(self, x=0, y=0):
        self.move(x, y)

    # Move method
    def move(self, x, y):
        self.x = x
        self.y = y

    # self is a manditory name.
    def reset(self):
        self.move(0, 0)

    # Calculate distance
    def calculate_distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))


if __name__ == "__main__":
    point = Point(3, 5)
    print(point.x, point.y)
