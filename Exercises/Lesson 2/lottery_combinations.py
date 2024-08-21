import math

def CalPossibleCombinations(n,r):
    combinations = math.factorial(n) * math.factorial(r) * math.factorial(n -r)
    return f"The number of possible combinations is {combinations}"

def main():
    while True:
        try:
            n = int(input("Enter the total number of available numbers (n): "))
            r = int(input("Enter the number of number to chosen (r): "))

            if r <= n:
                print("Invalid input. 'r' cannot be greater than 'n'. Please try again.")

            if
        except ValueError:
            pass

main()