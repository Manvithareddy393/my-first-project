import random
import string

def choose_word():
    return random.choice(string.ascii_lowercase)  # Choose a random lowercase letter

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Guess the letter: ", display_word(word, guessed_letters))

    while True:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha() or guess not in string.ascii_lowercase:
            print("Please enter a single lowercase letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            if display_word(word, guessed_letters) == word:
                print("Congratulations! You guessed the letter:", word)
                break
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1
            print("Attempts left:", max_attempts - incorrect_guesses)
            if incorrect_guesses == max_attempts:
                print("Sorry, you ran out of attempts. The letter was:", word)
                break

        print("Letter: ", display_word(word, guessed_letters))
        

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        hangman()
    else:
        print("Thanks for playing!")

hangman()
