# Promt the user to input length and width of billboard
# both input postive numbrs
# Pythagorean theorem formula to calculate the diagonal
import math


def calDiagonal(Length, Width):
    Diagonal = math.sqrt(Length ** 2 + Width ** 2)
    return f"The diagonal of the billboard is {Diagonal} meters."
def main():
    while True:
        try:
            length = float(input("Enter the length of the billboard (in meters): "))
            width = float(input("enter the width of the billboard (in meters): "))

            if length <= 0 or width <= 0:
                print("Invalid input. Please enter a positive number.")
                continue

            Diagonal = calDiagonal(length, width)

            print(f"\n{Diagonal}")
            break

        except ValueError:
            print("Invalid input. Please enter a numeric value")

main()