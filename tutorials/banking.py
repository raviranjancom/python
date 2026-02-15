# show balance
# withdraw
# deposit


def showBalance(balance):
    print(f"The Total Balance is {balance}")
    return balance

def withdraw(balance):
    amount=int(input("Enter the Amount to Withdraw : "))
    if balance>=amount:
        balance-=amount
        print("The Cash Withdrawal is Succesful")
    else:
        print("Insufficent Balance")
    return balance
    

def deposit(balance):
    amount=int(input("Enter the amount to be diposited : "))
    if(amount<0):
        balance+=amount
    else:
        print("Invalid amount")
    return balance

def main():
    balance=0
    print("---------- WELCOME ----------")
    while(True):
        print()
        print("1. Show Balance")
        print("2. Withdraw")
        print("3. Deposit")
        option_no=input("Choose an option (q to quit): ")
        if(option_no=="q"):
            break
        
        match(option_no):
            case '1':
                balance=showBalance(balance)
            case '2':
                balance=withdraw(balance)
            case '3':
                balance=deposit(balance)
            case _:
                print("Invalid option")

        print("--------------------------")

if __name__=="__main__":
    main()
