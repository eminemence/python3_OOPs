class Point:
    # self is a manditory name.
    def reset(self):
        self.x = 0
        self.y = 0


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
