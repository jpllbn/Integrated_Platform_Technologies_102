import math

def CalSquareRoot():
    while True:
        try:
            number = float(input("Enter a positive number to find its Square Root: "))
            if number <= 0:
                print("Invalid input. Please enter a postive number.")
                continue
            return number, math.sqrt(number)
        except ValueError:
            print("Invalid input. Please enter a numeric value")

def CalFactorial():
    while True:
        try:
            number = int(input("Enter a non-negative number to find its Factorial: "))
            if number <= 0:
                print("Invalid input. Please enter a postive number.")
                continue
            return number, math.factorial(number)
        except ValueError:
            print("Invalid input. Please enter a numeric value")
def main():
    print("Select an operation:")
    print("1. Square Root")
    print("2. Factorial")

    while True:
        try:
            user = int(input("Enter a choice (1-2): "))
            if user not in [1,2]:
                print("Invalid Choice. Please select 1 or 2")
                continue

            if user == 1:
                number, result = CalSquareRoot()
                print(f"\n Square Root of {number} is {result:.2f}")
            elif user == 2:
                number, result = CalFactorial()
                print(f"\n Factorial of {number} is {result:.2f}")
                continue
            break
        except ValueError:
                print("Invalid Input. Please enter number (1 or 2): ")
main()