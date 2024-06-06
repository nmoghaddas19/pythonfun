# celsius to fahrenheit converter
celsius = input("Enter temperature in celsius")
celsius = float(celsius)
fahrenheit = (9/5) * celsius + 32
print("Temperature in fahrenheit is", fahrenheit, "F")

# area of trapezoid calculator
height = float(input("Enter height"))
width_1 = float(input("Enter the first width"))
width_2 = float(input("Enter the second width"))
trapezoid_area = 0.5 * (width_1 + width_2) * height
print("Area of trapezoid is", trapezoid_area)

# area of arbitrary triangle
# import math
side_1 = float(input("Enter length of first side"))
side_2 = float(input("Enter length of second side"))
angle = float(input("Enter angle between them"))
angle_radians = math.radians(angle)
area = 0.5 * side_1 * side_2 * math.sin(angle_radians)
print("Area of triangle is", area)
this is a cool edit