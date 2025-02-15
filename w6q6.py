def area_of_triangle(a,b,c):
    s=((a+b+c)/2)
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))
    if(a==b==c):
        print("It is equilateral triangle.\nArea:", area)
    elif(a==b or a==c or b==c):
        print("It is isosceles triangle.\nArea: ", area)
    else:
        print("It is scalene triangle. \nArea: ", area) 
import math
print("To calculate the area of a triangle and specify it's type-")
a=int(input("enter first side of triangle: "))
b=int(input("enter second side of triangle: "))
c=int(input("enter third side of triangle: "))
area_of_triangle(a,b,c)