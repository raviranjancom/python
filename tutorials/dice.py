import random

options={
         1:("┌─────────┐","│         │","│    0    │","│         │","└─────────┘"),
         2:("┌─────────┐","│         │","│  0   0  │","│         │","└─────────┘"),
         3:("┌─────────┐","│    0    │","│    0    │","│    0    │","└─────────┘"),
         4:("┌─────────┐","│  0   0  │","│         │","│  0   0  │","└─────────┘"),
         5:("┌─────────┐","│  0   0  │","│    0    │","│  0   0  │","└─────────┘"),
         6:("┌─────────┐","│  0   0  │","│  0   0  │","│  0   0  │","└─────────┘")
        }

score=0
while(True):
    print("......... GAME .........")
    n=int(input("Enter the Number of Dice Rolls (q to Quit): "))
    if(n=="q" or n>5):
        
        print("Wrong input Try again!...")
        break
    if(n.is_integer()):
        score=0
        for i in range(n):
            value=random.randint(1,6)
            score+=value
            for edge in range(5):
                print(options[value][edge],end="\n")
        print(f"Total = {score}")
