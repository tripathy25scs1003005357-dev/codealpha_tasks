import random

# List of predefined words
words = ["python", "laptop", "banana", "coding", "camera"]

# Randomly choose a word
word = random.choice(words)

# Variables
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# Display hidden word
hidden_word = ["_"] * len(word)

print(" Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

# Game loop
while wrong_guesses < max_wrong_guesses and "_" in hidden_word:

    print("\nWord:", " ".join(hidden_word))
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    guess = input("Enter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print(" Correct Guess!")

        for index in range(len(word)):
            if word[index] == guess:
                hidden_word[index] = guess
    else:
        print(" Wrong Guess!")
        wrong_guesses += 1

# Final Result
if "_" not in hidden_word:
    print("\n Congratulations! You guessed the word:", word)
else:
    print("\n Game Over!")
    print("The correct word was:", word)