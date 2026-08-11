str= input("enter the string: ")
print(f"the first and last charis : {str[0],str[-1]}")
rev= str[::-1]
print(f"the rev str:  {rev}")
if str == rev:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")

word= str.split()
print(len(word)) # find words length
print(word) #split the words into list of words