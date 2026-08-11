# correct_username = "admin"
# correct_password = "python123"
# count = 0
# while (username := input("Enter Username: ")) != correct_username or \
#       (password := input("Enter Password: ")) != correct_password:
#     print("Invalid Username or Password. Try Again.")
#     count += 1
#     if count == 3:
#         print("Account Locked")
#         break
# else:
#     print("Login Successful")


words = ["apple", "cat", "banana", "dog", "mango", "kiwi"]

count = len([word for word in words if (length := len(word)) > 4])

print("Count:", count)