def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_numbers(n):
    if n == 1:
        return 1
    return n + sum_numbers(n - 1)


def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)


print(f"Factorial of 5 = {factorial(5)}")
print(f"Sum of first 5 numbers = {sum_numbers(5)}")
print(f"2^5 = {power(2, 1)}")