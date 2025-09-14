import math

# Base class: Point
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other):
        if not isinstance(other, Point):
            raise TypeError("Argument must be of type Point")
        return math.hypot(self.x - other.x, self.y - other.y)

# Subclass: Vector
class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Both operands must be Vectors")
        return Vector(self.x + other.x, self.y + other.y)

# ✅ Demonstration
if __name__ == "__main__":
    # Create Point objects
    p1 = Point(2, 3)
    p2 = Point(5, 7)
    print("Point equality:", p1 == p2)
    print("Distance between points:", p1.distance_to(p2))
    print(p1)

    # Create Vector objects
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1)
    print(v2)

    v3 = v1 + v2
    print("Vector addition result:", v3)