value = "abc"

# Write your logic here
try:
    if value != int(value):
        print("invalid msg")
except  ValueError:
    print("value error")