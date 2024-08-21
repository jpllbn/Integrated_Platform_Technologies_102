with open('account.txt', 'r') as file:
    for line in file:
        line = line.strip()
        pin, name, Id, team = line.split('*')
        print(f"PIN: {pin} \nNAME: {name} \nID: {Id} \nTEAM: {team}\n")