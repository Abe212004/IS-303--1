from wordle_functions import choose_word, get_guess, evaluate_guess, display_guess, has_won
 
MAX_ATTEMPTS = 6
 
# Rules and game instructions
print("Welcome to Mystery Wordle!")
print("Guess the five-letter word.")
print("G = correct letter and position")
print("Y = correct letter, wrong position")
print("- = letter is not in the word")

#Replay feature
play_again = "yes"
while play_again == "yes":
    secret_word = choose_word()
    previous_guesses = []
    won = False

 #Game loop for 6 attempts
    for attempt in range(1, MAX_ATTEMPTS + 1):
        print(f"\nAttempt {attempt} of {MAX_ATTEMPTS}")
        guess = get_guess(previous_guesses)
        previous_guesses.append(guess)
 
        feedback = evaluate_guess(guess, secret_word)
        display_guess(guess, feedback)
 
        if has_won(guess, secret_word):
            won = True
            break 
 
    if won:
        print("Congratulations! You solved the puzzle.")
    else:
        print(f"Out of guesses. The word was {secret_word.upper()}.")
 
    play_again = input("\nWould you like to play again? ").lower().strip()
 
print("Thanks for playing!")
