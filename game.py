import random

#Allows for a player to play multiple times
play_again = "Y"
while play_again == "Y" or play_again == "y":

    # Computer generates a random number between 1 and 100 and sets baseline for guesses
    secret_num = random.randint(1, 100)
    num_guesses = 0
    guess = 0

    #Game starts
    print("I'm thinking of a number from 1 to 100.")
    while guess != secret_num:
        guess = int(input("Enter your guess: "))

        # Prevents guesses from outside of the range being counted
        while guess < 1 or guess > 100:
            print("Invalid guess. Please try again.")
            guess = int(input("Enter your guess: "))

        # Increment the number of correct guesses
        num_guesses += 1

        # Compare the guess to the secret number
        if guess > secret_num:
            print("Lower!")
        elif guess < secret_num:
            print("Higher!")
        else:
            print("Correct!")

    # The loop ends and the number of guesses is printed 
    print("You got it in", num_guesses, "guesses!")
    if num_guesses <= 3:
        print("Amazing!")
    elif num_guesses <= 5:
        print("Impressive!")
    elif num_guesses <= 7:
        print("Good job!")
    elif num_guesses <= 9:
        print("Took a little longer, but you got there!")
    else:
        print("You need to lock in.")

    # Ask the user if they want to play again
    play_again = input("Would you like to play again? (Y/N): ")
    print()