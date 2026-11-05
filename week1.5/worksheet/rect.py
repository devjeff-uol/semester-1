# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """
        # Add code here to check type and value of provided width & height,
        # raising appropriate exceptions if necessary (see README.md)

        if not (isinstance(width, (int)) and isinstance(height, (int))):
            raise TypeError("Both width and height should be integers")

        if not (width > 0 and height > 0):
            raise ValueError("Both width and height should be larger than 0") 

        self.width = width
        self.height = height

    # Implement methods is_square(), area() & perimeter() here
    def is_square(self):
        """
        Returns True if the rectangle is a square
        """
        return self.width == self.height
    
    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        return self.width * 2 + self.height * 2
