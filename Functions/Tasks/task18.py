numbers = [10, 20, 30, 40, 50]

square = list(map(lambda x: x ** 2, numbers))
greater = list(filter(lambda x: x > 25, numbers))
result2 = (max(numbers))
print(f"Original List : {numbers}")
print(f"square List   : {square}")
print(f"numbers greater than 25: {greater}")
print(f"the maximum number: {result2}")


