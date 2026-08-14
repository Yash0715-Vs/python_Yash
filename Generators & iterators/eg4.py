n = int(input("Enter n: "))

squares = (x * x for x in range(n + 1))

print("Squares:")

while True:
    try:
        print(next(squares))

    except StopIteration:
        break