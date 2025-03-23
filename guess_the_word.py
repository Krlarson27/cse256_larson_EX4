import random

word = ["python", "computer", "science", "programming", "github"]

def chose_word():
    return random.choice(word)

def display_word(word, guessed_letters):
    return "".join(letter if letter in guessed_letters else "_" for letter in word)

def play_game():
    word = chose_word()
    guessed_letters = set()
    attempts = len(word) + 3


    print("Welcome to the game of guessing the word!")
    print("Try to guess the word letter by letter.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        

    if guess in guessed_letters:
        print("You already guessed that letter.")
        

    guessed_letters.add(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Incorrect.")
        attempts -= 1

    if set(word).issubset(guessed_letters):
        print("Congratulations! You guessed the word:", word)
        return
    
    print("Game over man! The word was:", word)

if __name__ == "__main__":
    play_game()
