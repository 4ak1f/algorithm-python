print("Q2-Python function which accepts the radius of a sphere and computes the volume. What is the volume of a sphere with radius 5?")
def sphere_vol(rad):
    print("Volume of Sphere is: ", (4/3)*math.pi*rad*rad*rad)

import math
r=int(input("Enter the radius of the sphere to get it's volume: "))
sphere_vol(r)