class InsufficientBalanceError(Exception):
    pass

balance = 10000
amount = 15000

try:
    if balance < amount:
        raise InsufficientBalanceError ("insufficient balance")
    else:
        print("amount is high")
except InsufficientBalanceError as e:
    print(e)