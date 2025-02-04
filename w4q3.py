print("Q3-Enter the radius of a circle to compute the area.")
import math
def circle_area(radius):
    return math.pi * radius**2

print("Calculate the area of a circle")
radius = float(input("Enter the radius of the circle: "))
print("Area of circle:", circle_area(radius))