import random

def game_win(computer: str, you: str) -> bool:
    if computer == you:
        return None
    elif computer == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif computer == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif computer == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

def main() -> None:
    print("Computer's Turn: Choose Snake(s), Water(w), Gun(g): ")
    rand_no: int = random.randint(1, 3)
    if rand_no == 1:
        computer: str = "s"
    elif rand_no == 2:
        computer: str = "w"
    elif rand_no == 3:
        computer: str = "g"

    you: str = input("Your Turn: Choose Snake(s), Water(w), Gun(g): ")

    print(f"You chose {you}")
    print(f"Computer chose {computer}")
    
    result: bool = game_win(computer, you)
    if result is None:
        print("Game tied!")
    elif result:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    main()
