def countdown(n):
    while n > 0:
        yield n
        n -= 1
    for num in countdown(5):
        print(num)
squares_gen = (x*x for x in range(5))
print(list(squares_gen))
