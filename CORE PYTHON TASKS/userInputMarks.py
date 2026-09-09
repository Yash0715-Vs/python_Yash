n= int(input("enter the marks: "))
if n>=90 and n<=100:
    print("A")
elif n>=80 and n<90:
    print("B")
elif n>=60 and n<80:
    print("C")
elif n>=40 and n<60:
    print("D")
elif n<40:
    print("fail")
elif n>100:
    print("Invalid marks")
else:
    print("error")
    