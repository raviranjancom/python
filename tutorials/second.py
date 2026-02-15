# import random
# low=1
# high=5

# turn=0
# while(True):
#     turn+=1
#     print("............GAME............")
#     guess=random.randint(low,high)
#     value=int(input("Enter your guess : "))
#     print()
#     if(guess!=value):
#         print("Wrong! Try again...")
#     else:
#         print(f"You Win in turn = {turn}")
#         break

import random

options=("rock", "paper", "sissors")

score=0
total=0
while True:
    total+=1
    print("............ GAME ............")
    n=random.choice(options)
    guess=input("Enter (Rock, Paper, Sissors) or (q to Quit): ")
    if(guess=="q"):
        break

    elif(guess==n):
        print("It's a Tie!")
    elif(guess=="rock" and n=="sissors") or (guess=="paper" and n=="rock") or (guess=="sissors" and n=="paper"):
        print("You Win! ")
        score+=1
    else:
        print("AI Wins")
    print()
    print(f"AI = {n}  USER = {guess}")
    print()
print(f"Score = {score}/{total}")
