import MyPackage.atm_transactions as ATM

def menu():
    print('=' * 10, "ATM TRANSACTIONS", '=' * 10)
    print("[C] - Check Balance")
    print("[D] - Deposit")
    print("[W] - Withdraw   ")
    print("[X] - Exit")

def main():
    print('='*10, "LOGIN ACCOUNT", '='*10)
    while True:
        Accounts = {}
        try:
            NoOfTries = 0
            with open('account.txt', 'r') as BankAccount:
                for line in BankAccount:
                    line = line.strip()
                    AccountNumber, AccountPin, AccountName, AccountBalance = line.split('#')

                    Accounts['AccountNumber'] = AccountNumber
                    Accounts['AccountPin'] = AccountPin
                    Accounts['AccountName'] = AccountName
                    Accounts['AccountBalance'] = AccountBalance

            user = int(input("Enter PIN: "))

            if user == Accounts['AccountPin'] in Accounts:
                print(f"Welcome {Accounts['AccountName']}")
                continue
                
            print(f"Welcome {Accounts['AccountName']}")

        except FileNotFoundError:
            print("File not Exist")



if __name__ == '__main__':
    main()


