import datetime

today = datetime.date.today()
print(today.strftime("%d-August-%Y"))
print(today.strptime("2026,1,7"))
