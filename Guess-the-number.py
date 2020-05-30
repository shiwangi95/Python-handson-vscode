import random

def generate_random():
    lst1 = [str(i) for i in range(0,10)]
    random.shuffle(lst1)
    return lst1[:3]

def generate_guess():
    guess = input("Enter your guess :")
    return list(guess)

def generate_hints(guess,random):

    hints = []
    if guess == random:
        return guess

    for index,item in enumerate(random):
        if guess[index] == item:
            hints.append("Match")
        elif item in guess:
            hints.append("Close")
    if hints == []:
        hints.append("None")

    return hints


print("Welcome to the number-guessing game !!")
random = generate_random()
#print(random)
print("The bot has guessed a number . Can you tell what is it ?? LET'S GO")
hints = []
while hints != random:

    guess = generate_guess()
    print("Here is the result of your guess :")
    hints = generate_hints(guess,random)
    for h in hints:
        print(h)

else:
    print("CODE CRACKED!!!!!!!!!!!!!!")