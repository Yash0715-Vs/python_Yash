number = [i for i in range(1,11)]
print(number)

square = [i**2 for i in range(1,5)]
print(square)

even = [i for i in range(1,11) if i%2==0]
print(even)

marks =[22,33,44,55,66,77,88]
greater_marks = [i for i in marks if i>50]
print(greater_marks)

words =["Python", "Java", "C++", "HTML"]
length_of_words = [len(i) for i in words]
print(length_of_words)


words = ["apple", "banana", "kiwi", "mango"]

new_list = [word.upper() if len(word) > 5 else word.lower() for word in words]

print(new_list)