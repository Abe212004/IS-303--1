import random
 
# Secret words: all five letters, no repeated letters
word_list = ["plant", "crane", "slate", "house", "brick",
             "light", "mouse", "ghost", "chair", "stone"]
 
 
# Pick a random word from the list and return it
def choose_word():
    return random.choice(word_list)
 
 
# Ask for a guess until it is 5 letters, letters only, and not already used.
# previous_guesses is the list of words the player has already tried.
def get_guess(previous_guesses):
    guess = input("Enter a five-letter word: ").lower().strip()
    while len(guess) != 5 or not guess.isalpha() or guess in previous_guesses:
        if len(guess) != 5 or not guess.isalpha():
            print("Your guess must be exactly five letters. Try again.")
        else:
            print("You already guessed that word. Try a different one.")
        guess = input("Enter a five-letter word: ").lower().strip()
    return guess
 
 
# Compare the guess to the secret word one position at a time.
# Returns a list of 5 symbols: "G", "Y" or "-"
def evaluate_guess(guess, secret_word):
    feedback = []
    for i in range(len(secret_word)):
        if guess[i] == secret_word[i]:
            feedback.append("G")        # right letter, right spot
        elif guess[i] in secret_word:
            feedback.append("Y")        # right letter, wrong spot
        else:
            feedback.append("-")        # letter not in the word
    return feedback
 
 
# Print the guess and its feedback with spaces between letters
def display_guess(guess, feedback):
    print("Guess:", " ".join(guess.upper()))
    print("Feedback:", " ".join(feedback))
 
 
# Return True if the guess matches the secret word, otherwise False
def has_won(guess, secret_word):
    return guess == secret_word