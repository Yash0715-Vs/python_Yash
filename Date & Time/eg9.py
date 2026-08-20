from datetime import datetime

birthday = datetime.strptime("20-08-2028","%d-%m-%Y")

today= datetime.now()

diff = birthday - today

print(f"diff is: {diff.days}")
print(birthday.strftime("%A, %d %B %Y"))