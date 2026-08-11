list =[10, 20, 20, 30, 30, 40]
set ={i for i in list}
print(set)

words = ["apple", "banana", "kiwi", "mango"]

new_list = {word.upper() for word in words}
print(new_list)

words = ["Apple", "Banana", "APPLE", "banana", "Kiwi"]
set ={word.lower() for word in words}
print(set)