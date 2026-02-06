# Lab 3 - Object Oriented Programming (OOP)
# Author: Wenyu Zhang

from abc import ABC, abstractmethod
import math

# -------------------------
# Base Shape class
# -------------------------
class Shape(ABC):
    """
    Abstract base class for all shapes.
    Each shape must implement getArea() and __str__().
    """
    @abstractmethod
    def getArea(self) -> float:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

# Rectangle class
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def getArea(self) -> float:
        return self.length * self.width

    def __str__(self) -> str:
        return f"Rectangle(length={self.length}, width={self.width})"

# Triangle class
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def getArea(self) -> float:
        return 0.5 * self.base * self.height

    def __str__(self) -> str:
        return f"Triangle(base={self.base}, height={self.height})"

# Circle class
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def getArea(self) -> float:
        return math.pi * (self.radius ** 2)

    def __str__(self) -> str:
        return f"Circle(radius={self.radius})"

# Parse one line from input file
def parse_shape_line(line: str) -> Shape | None:
    """
    Expected formats (comma-separated):
      Rectangle,8,4
      Triangle,8,1
      Circle,3
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    parts = [p.strip() for p in line.split(",")]
    shape_name = parts[0].lower()

    # Create object by shape type
    if shape_name == "rectangle":
        length = float(parts[1])
        width = float(parts[2])
        return Rectangle(length, width)

    if shape_name == "triangle":
        base = float(parts[1])
        height = float(parts[2])
        return Triangle(base, height)

    if shape_name == "circle":
        radius = float(parts[1])
        return Circle(radius)

    # Unknown shape type
    raise ValueError(f"Unknown shape type: {parts[0]}")


def main():
    # Path to input file
    input_file = "lab_3\\shape.txt"

    shape: list[Shape] = []

    # Read file (required by rubric)
    with open(input_file, "r") as f:
        for line_num, line in enumerate(f, start=1):
            try:
                obj = parse_shape_line(line)
                if obj is not None:
                    shape.append(obj)
            except Exception as e:
                print(f"[Warning] Skipped line {line_num}: {e}")

    # Print the area of each shape
    print("=== Shape Areas ===")
    for i, s in enumerate(shape, start=1):
        print(f"Area of {s} is {s.getArea():.2f}")


if __name__ == "__main__":
    main()