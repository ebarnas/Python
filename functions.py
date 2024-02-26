# Function to calculate the area of a square
def square(side):
    area = side * side
    print("The area of the square is " + str(area) + " square units.")

# Function to calculate the area of a circle
def circle(radius):
    π = 3.14
    area = π * radius * radius
    print("The area of the circle is " + str(area) + " square units.")

# Testing the functions with sample values
square(10)
circle(2)