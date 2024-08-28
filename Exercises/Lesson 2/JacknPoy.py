import random

def ComputerChoice():
    choices = random.randint(1,3)
    if choices == 1:
        return "rock"
    elif choices == 2:
        return "scissor"
    elif choices == 3:
        return "paper"
    else:
        return "draw"

def WhoisWinner(PlayerChoice, ComputerChoice):
    if PlayerChoice == ComputerChoice:
        return "It's a draw!"
    elif (PlayerChoice == "rock" and ComputerChoice == "scissor") or \
        (PlayerChoice == "scissor" and ComputerChoice == "paper") or \
        (PlayerChoice == "paper" and ComputerChoice == "rock"):
        return "You Win"
    else:
        return "Computer Wins"

def main():
    print("Welcome to Jack n Poy! (Rock, Paper, Scissors)")

    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if player_choice not in ["rock", "paper", "scissor"]:
            print("Invalid choice! Please choose rock, paper, scissors.")
            continue

        computer_choice = ComputerChoice()
        print(f"Computer chose: {computer_choice}")

        result = WhoisWinner(player_choice, computer_choice)

        print(result)


if __name__ == '__main__':
    main()