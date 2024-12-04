class Rectangle:
    def __init__(self, length, width):
        """
        Initialize the Rectangle with length and width.
        """
        self.length = length
        self.width = width

    def calculate_area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.length * self.width

    def calculate_perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def is_square(self):
        """
        Check if the rectangle is a square.
        """
        return self.length == self.width


# Example Usage
# Create a rectangle object
rect = Rectangle(10, 5)

# Calculate area
area = rect.calculate_area()
print(f"Area: {area}")

# Calculate perimeter
perimeter = rect.calculate_perimeter()
print(f"Perimeter: {perimeter}")

# Check if it's a square
is_square = rect.is_square()
print(f"Is it a square? {'Yes' if is_square else 'No'}")

# Create a square object for testing
square = Rectangle(6, 6)
print(f"\nFor a rectangle with length {square.length} and width {square.width}:")
print(f"Area: {square.calculate_area()}")
print(f"Perimeter: {square.calculate_perimeter()}")
print(f"Is it a square? {'Yes' if square.is_square() else 'No'}")
