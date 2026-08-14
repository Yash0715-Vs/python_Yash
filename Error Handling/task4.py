student = {
    "name": "Yash",
    "marks": 85
}
try:
    dict= (input("enter the key: "))
    print(f"the key is: {student[dict]}")
except KeyError:
    print("plz enter the vadil key")