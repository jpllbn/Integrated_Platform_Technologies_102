def compound_interest(P, AnInt, CompYr, NumOfYrsInvsted):
    amount = P * NumOfYrsInvsted * (1 + AnInt / CompYr)
    return amount
def main():
    while True:
        try:
            P = int(input("Enter the principal amount: "))
            AnInt = float(input("Enter the annual interest rate (as a decimal): "))
            CompYr = int(input("Enter the number of times interest is compounded per year: "))
            NumOfYrsInvsted = int("Enter the number of years the money for: ")

            if P < 0 or AnInt < 0 or CompYr < 0 or NumOfYrsInvsted < 0:
                print("Invalid input. Please enter a postive number.")
                continue

            Total = compound_interest(P, AnInt, CompYr, NumOfYrsInvsted)
            print(f"Total accumulated amount after {NumOfYrsInvsted} years: {Total}")
        except ValueError:
            print("Invalid input. Please enter a valid value.")

main()