s = input("Enter a string: ")

rev = s[::-1]
# negative slicing

if s == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

print(f"Reverse: {rev}")