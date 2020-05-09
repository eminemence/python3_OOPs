import math


class Point:
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


p1 = Point()
p2 = Point()

# Adding x,y attribute to Point P1
p1.x = 5
p1.y = 4

p2.reset()
print(p2.x, " ", p2.y)
# Adding x,y attribute to Point P1
p2.x = 3
p2.y = 6

print(p1.x, " ", p1.y)
print(p2.x, " ", p2.y)

p1.reset()
print(p1.x, " ", p1.y)

# Showing the use of self
Point.reset(p2)
print(p2.x, " ", p2.y)

# Calculate distance
point1 = Point()
point2 = Point()

point1.reset()
point2.move(5, 0)
print(point2.calculate_distance(p1))

#  The program asserts when the below line is false, and exits with AssertionError
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

point1.move(3, 4)
print(point2.calculate_distance(p1))
