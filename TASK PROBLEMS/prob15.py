marks=[33,44,66,77,88,99,89,77]
print(f"Largest number: {max(marks)}") #greater
print(f"Smallest number: {min(marks)}")#lower
average = sum(marks)/len(marks)
print(average)

if marks[0]>=75 :
    print("you pass!")
elif marks[1]>=75:
    print("you pass!")
elif marks[2]>=75:
    print("you pass!")
elif marks[3]>=75:
    print("you pass!")
elif marks[4]>=75:
    print("you pass!")
elif marks[5]>=75:
    print("you pass!")
elif marks[6]>=75:
    print("you pass!")
elif marks[7]>=75:
    print("you pass!")
else:
    print("you fail")