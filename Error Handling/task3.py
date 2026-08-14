numbers = [10, 20, 30, 40, 50]
try:
    index= int(input("enter the index"))
    print(f"the index: {numbers[index]}")
except IndexError:
    print("Invalid index! Please enter an index between 0 and 4.")