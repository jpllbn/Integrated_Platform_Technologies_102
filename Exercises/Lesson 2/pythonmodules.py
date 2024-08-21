# import arithmetic_operations as AR
#
# try:
#     FirstNumber = float(input("Enter the first number: "))
#     SecondNumber = float(input("Enter the second number: "))
#
#     print("Results:")
#     print("Addition: ", AR.Add(FirstNumber, SecondNumber))
#     print("Subraction: ", AR.Subtract(FirstNumber, SecondNumber))
#     print("Multiplication: ", AR.Multiply(FirstNumber, SecondNumber))
#     print("Division: ", AR.Division(FirstNumber, SecondNumber))
# except ZeroDivisionError:
#     print("Division: Error: Division by zero is undefined.")

# import math
#
# def calCircumference(radius):
#     circumference = 2 * math.pi * radius
#     return circumference
#
# def main():
#     while True:
#         try:
#             radius = float(input("Enter the radius of the circle: "))
#             if radius <= 0:
#                 print("Invalid input. Please enter a positive number.")
#                 continue
#             break
#         except ValueError:
#             print("Invalid input. Please enter a positive number.")
#
#
#     circumference = calCircumference(radius)
#     print(f"Calculations for a circle with radius {circumference}:")
#     print('-'*40)
#     print(f"Circumference: {circumference:.2f} units")
#
# main()

import math

def calArea(radius):
    area = math.pi* (radius**2)
    return area

def main():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                print("Invalid input. Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive number.")


    area = calArea(radius)
    print(f"Calculations for a circle with radius {radius}:")
    print('-'*40)
    print(f"Area: {area:.2f} units")

main()
