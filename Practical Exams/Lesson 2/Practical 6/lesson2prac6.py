import math

def CalAreaCircle():
    while True:
        try:
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                print("Invalid input. Please enter a positive number.")
                continue

            area = math.pi * (radius**2)
            print(f"\n Calculation for a circle with radius {radius}")
            print('-' * 40)
            print(f"Area: square {area:.2f} square units")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value")

def CalSurfaceAreaCylinder():
    while True:
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder"))
            if radius <= 0:
                print("Invalid input. Please enter a positive number.")
                continue

            SurfaceArea = math.pi * 2 * radius * (radius+height)
            print(f"\n Calculation for a cylinder with radius {radius} and height {height}")
            print('-' * 40)
            print(f"Surface Area: {SurfaceArea:.2f} square units")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value")

def CalVolumeCylinder():
    while True:
        try:
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder"))
            if radius <= 0:
                print("Invalid input. Please enter a positive number.")
                continue
            Volume = math.pi * radius ** 2 * height
            print(f"Volume: {Volume:.2f} square units")
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value")

def CalSurfaceAreaCone():
    pass

def CalVolumeCone():
    pass

def main():
    print("Select a Shape to shape to calculate:")
    print("1. Circle (Area)")
    print("2. Cylinder (Surface Area and Volume")
    print("3. Cone (Surface Area and Volume")

    while True:
        try:
            user = int(input("Enter a choice (1-3): "))
            if user not in [1,2, 3]:
                print("Invalid Choice. Please select 1 or 2 or 3")
                continue

            if user == 1:
                CalAreaCircle()
            elif user == 2:
                CalSurfaceAreaCylinder()
                CalVolumeCylinder()
                print(f"\n ")
            elif user == 3:
                pass
                print(f"\n ")
                continue
            break
        except ValueError:
                print("Invalid Input. Please enter number (1 or 2): ")
main()