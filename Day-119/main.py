import random

# List of words for the game
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

# Function to choose a random word from the list
def choose_word(word_list):
    return random.choice(word_list)

# Function to play Hangman
def hangman():
    word_to_guess = choose_word(word_list)
    guessed_letters = []
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    
    while True:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"Word to guess: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        if display_word == word_to_guess:
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
        
        if attempts == 0:
            print("Sorry, you're out of attempts. The word was:", word_to_guess)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_to_guess:
            guessed_letters.append(guess)
        else:
            guessed_letters.append(guess)
            attempts -= 1
            print("Incorrect guess!")

# Main function
if __name__ == "__main__":
    hangman()
