n = int(input("enter the number: "))#user input for number
if n>0:

    if n%2!=0:
        result= n +10
        print("positive odd number") 
        print(f"result is: {result}")
    else:
        result = n*2.5
        print("positive even number")
        print(f"result is: {result}")

elif n<0:
    if n%2!=0:
        result= n - 10
        print("negative odd number")
        print(f"result is: {result}")
    else:
        result = n/2.5
        print("negative even number")
        print(f"result is: {result}")

else:
    print("number is zero")
