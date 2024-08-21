while True:
    try:
        record = 0
        with open('account.txt', 'r') as BankAccount:
            for line in BankAccount:
                line = line.strip()
                AccountNumber, AccountName, AccountBalance, Pin = line.split('#')
                for _ in AccountNumber, AccountName, AccountBalance, Pin:
                    record += 1
                    print(f"Record No. {record}")
                    print(f"Account No: {AccountNumber}\nAccount Name: {AccountName}\nAccount Balance: {AccountBalance}\nPin: {Pin}\n")
                    print("-------------------------------------------------------------")
                    break
            break
    except FileNotFoundError:
        print("File not Exist")
