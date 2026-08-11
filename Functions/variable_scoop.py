# def hello():
#     name ="suthar"# local variable
#     print(name)

# hello()

# name= "yash"#grobal variable
# def hello():
#     print(name)
# hello()

# count = 0
# def increace():
#     global count
#     count+=5
#     print(count)

# increace()
# increace()

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
        print(amount)
    else:
        print("insufficiant balance")

deposite(3000)
withdraw(500)

print(f"balance : {balance}")