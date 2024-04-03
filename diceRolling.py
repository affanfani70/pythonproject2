import random


def dice_rolls(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError
    rolls: list[int] = []
    for i in range(amount):
        random_rolls: int = random.randint(1, 6)
        rolls.append(random_rolls)
    return rolls


def main():
    while True:
        try:
            user_input = input("Enter the number of dice OR enter exit to end the game: ")
            if user_input.lower() == 'exit':
                print("Thanks for playing!")
                break

            result = dice_rolls(int(user_input))
            print(*result, sep=', ')
        except ValueError:
            print("Please Enter the Valid number")


if __name__ == '__main__':
    main()
