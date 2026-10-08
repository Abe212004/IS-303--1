import random

lChoices = ["rock", "paper", "scissors"]
 
# Ask for a choice and convert it to lowercase, make sure it's right and return it
def get_player_choice():
    sChoice = input("Enter rock, paper, scissors: ").lower().strip()
    while sChoice not in lChoices:
        print(f'Sorry, "{sChoice}" is not a valid choice. Please try again.')
        sChoice = input("Enter rock, paper, scissors: ").lower().strip()
    return sChoice
 
 
# Compare the player's choice to the computer's and return "win", "loss", or "tie"
def determine_winner(sPlayer, sComputer):
    if sPlayer == sComputer:
        return "tie"
    elif (sPlayer == "rock" and sComputer == "scissors") or \
         (sPlayer == "paper" and sComputer == "rock") or \
         (sPlayer == "scissors" and sComputer == "paper"):
        return "win"
    else:
        return "loss"
 
 
# Main Program
print("Welcome to Rock Paper Scissors!")
 
iRounds = int(input("How many rounds would you like to play: "))
while iRounds <= 0 or iRounds % 2 == 0:
    iRounds = int(input("Sorry, the number must be an odd number. Please try again: "))
 
iPlayerWins = 0
iComputerWins = 0
 
# Ties don't count, so keep playing until the decided rounds add up to iRounds
while iPlayerWins + iComputerWins < iRounds:
    sPlayer = get_player_choice()
    sComputer = random.choice(lChoices)
    print(f"The computer chose {sComputer}.")
 
    sResult = determine_winner(sPlayer, sComputer)
    if sResult == "win":
        print("You won!")
        iPlayerWins += 1
    elif sResult == "loss":
        print("You lost!")
        iComputerWins += 1
    else:
        print("Tie! Play again.")
 
print("-------------------------------------------")
print(f"Score — You: {iPlayerWins} | Computer: {iComputerWins}")
if iPlayerWins > iComputerWins:
    print("You win!!!")
else:
    print("The computer wins!")
print("Thanks for playing!")