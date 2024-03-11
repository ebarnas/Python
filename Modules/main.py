from math_operations import calculator, geometry

result = calculator.add(5, 3)
print("Addition result:", result)

result = calculator.subtract(10, 4)
print("Subtraction result:", result)

area_rectangle = geometry.rectangle_area(4, 6)
print("Rectangle area:", area_rectangle)

area_triangle = geometry.triangle_area(5, 8)
print("Triangle area:", area_triangle)

area_circle = geometry.circle_area(3)
print("Circle area:", area_circle)