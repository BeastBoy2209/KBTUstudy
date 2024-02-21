#required libraries
import math
#1
degree = input("input degree:")
degree = float(degree)
radians = math.radians(degree)
print("Radians: ", radians)
#2
def calculate_trapezoid_area():
    base1 = float(input("Enter the length of the first base: "))
    base2 = float(input("Enter the length of the second base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * (base1 + base2) * height
    print("The area of the trapezoid is: ", area)

calculate_trapezoid_area()
#3
import math

def calculate_polygon_area():
    n = int(input("Enter the number of sides: "))
    s = float(input("Enter the length of a side: "))
    area = (0.25 * n * s**2) / math.tan(math.pi/n)
    print("The area of the regular polygon is: ", round(area))

calculate_polygon_area()
#4
def calculate_parallelogram_area():
    base = float(input("Enter the length of the base: "))
    height = float(input("Enter the height: "))
    area = base * height
    print("The area of the parallelogram is: ", area)

calculate_parallelogram_area()

