import math


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def perimeter(polygon):
    perimeter = 0
    points = polygon + [polygon[0]]
    print(points)
    for i in range(len(polygon)):
        perimeter += distance(points[i], points[i + 1])
    return perimeter


if __name__ == "__main__":
    square = [(1, 1), (1, 2), (2, 2), (2, 1)]
    print(perimeter(square))
