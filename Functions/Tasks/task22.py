def analyze(*numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    even_count = 0
    odd_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return largest, smallest, total, average, even_count, odd_count


# User Input
nums = input("Enter numbers separated by spaces: ")

numbers = tuple(map(int, nums.split()))

# Function Call
largest, smallest, total, average, even, odd = analyze(*numbers)

print(f"Largest Number  : {largest}")
print(f"Smallest Number : {smallest}")
print(f"Sum             : {total}")
print(f"Average         : {average:.2f}")
print(f"Even Count      : {even}")
print(f"Odd Count       : {odd}")