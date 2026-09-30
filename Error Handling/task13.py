number = 25
try:
    result = 100/number

    
except ZeroDivisionError:
    print("error ocurs")

else:
    print(f"result: {result}")

finally:
    print("program finish")