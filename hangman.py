import random


def run_game():
    words = random.choice(["apple", "banana", "cherry", "grapes", "orange"])
    username = input("Enter your name: ")
    print("Welcome " + username + "!")

    guesses: str = ""
    tries: int = 3
    while tries > 0:
        blanks: int = 0
        print("word", end="")
        for letter in words:
            if letter in guesses:
                print(letter)
            else:
                print("_", end="")
                blanks += 1

        print()
        if blanks == 0:
            print("You won!")
            break

        guess: str = input("Guess a letter: ")
        if guess in guesses:
            print("You already guessed")
            continue

        guesses += guess

        if guess not in words:
            tries -= 1
            print(f"guess is not in the word and ({tries} left)")
            if tries == 0:
                print("No, attempts left")
                break


if __name__ == "__main__":
    run_game()
