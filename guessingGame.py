import random
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
chances=0
print("GUESS THE NUMBER BETWEEN 1 TO 9 ")
while chances<5:
    guess = int(input("enter your guess:- "))
    if guess == number :
        print("congratulations u  won")
    elif guess<number:
        print("your guess is to low guess the higher numner")
    elif guess>number:
        print("your guess is very high guess a lower number")
    chances +=1
if not chances<5:
    print("ohh!! you lose!!the number is ",number)
    