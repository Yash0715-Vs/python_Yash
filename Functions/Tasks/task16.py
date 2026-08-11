balance = 1000
def deposite(amount):
    global balance
    balance+= amount
    return balance

def withdraw(amount):
    global balance

    if amount<=balance:
        balance-=amount
        print(balance)
        return amount
    else:
        return "insufficiant_balance"

def check_balance():
    return balance

while True:
    print("1. deposite")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")

    choice = int(input("enter your choice(1-4)"))

    if choice == 4:
        print("exit")
        break

    elif choice == 1:
        amount= float(input("enter the deposite amount: "))
        print(f"the update ammount: {deposite(amount)}")

    elif choice == 2:
        amount= float(input("enter the withdraw amount: "))
        print(f"the withdraw amount: {withdraw(amount)}")
        

    elif choice == 3:
        print(f"Current Balance = {check_balance()}")

    else:
        print("invalid choice")
    