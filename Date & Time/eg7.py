from datetime import datetime

date = datetime.strptime("20-08-2028","%d-%m-%Y")

today= datetime.now()

diff = date - today

print(f"diff is: {diff.days}")