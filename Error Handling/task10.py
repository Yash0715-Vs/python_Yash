numbers = [10, 20, 30]
index = 5

# Write your logic here
try:
    numbers = [10, 20, 30]
    print(numbers[index])
except IndexError:
    print("index not found")