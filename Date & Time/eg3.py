import datetime

today = datetime.date.today()
future = today + datetime.timedelta(weeks=1)
print(future)