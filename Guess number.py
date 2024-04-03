import random
randNumber = random.randint(1,100)
userGuess = None
guesses = 0
while userGuess != randNumber:
    userGuess = int(input("Enter your Guess: "))
    guesses +=1
    if userGuess == randNumber:
        print("You guess the right number.")
    else:
        if userGuess > randNumber:
            print("Enter the samller Number... ")
        else:
            print("Enter the higher Number... ")

print(f"your score is {guesses}")

with open('project2.txt','r') as f:
    highScore = int(f.read())

if guesses > highScore:
    with open('project2.txt','w') as f:
        f.write(str(guesses))