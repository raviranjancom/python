import random as r

def spin():
    fruits=["🍎","🍊","🍏","🍉","🍇","🍋‍🟩"]
    length=len(fruits)-1
    a=r.randint(0,length)
    b=r.randint(0,length)
    c=r.randint(0,length)

    print(f"{a} {b} {c}")

    return a==b and b==c

def get_paycheck(balance):
    amount=int(input("Enter the amount : "))
    if(amount>0 and balance >= amount):
        balance-=amount
        print("Amount Withdraw Succesfully")
    else:
        print("Insufficent amount!")
    
    return balance

def main():
    balance=100
    running=True

    while(running):
        print("---------- GAME ----------")
        print()
        print(f"Balance amount = {balance}")
        bet_amount = input("Enter the bet amount (q to quit): ")
        if (bet_amount.lower()=='q'):
            running=False
        elif(not bet_amount.isdigit()):
            print("Enter valid Amount!")
        elif(balance>=int(bet_amount)):
            win=spin()
            if(win):
                balance+=int(bet_amount)
                print("You Win")

                if("y"==input("Do you want to get_paycheck (y / n): ").lower()):
                    balance=get_paycheck(balance)
            else:
                balance-=int(bet_amount)
                print("You Lose!")
        else:
            print("Insufficent Balance")
            

if __name__=="__main__":
    main()
