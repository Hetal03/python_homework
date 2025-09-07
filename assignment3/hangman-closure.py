def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        # Show guessed letters and underscores for unguessed
        display = ''.join([char if char in guesses else '_' for char in secret_word])
        print("Current word:", display)

        # Check if word is fully guessed
        return set(secret_word).issubset(set(guesses))

    return hangman_closure


# Game execution logic
if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").lower()
    print("\n" * 50)  # Clear screen so other player can't see secret word

    game = make_hangman(secret_word)
    guessed_correctly = False

    while not guessed_correctly:
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical letter.")
            continue

        guessed_correctly = game(guess)

    print(f"\nCongratulations! You've guessed the word: {secret_word}")