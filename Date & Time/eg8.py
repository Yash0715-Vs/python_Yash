from datetime import datetime, timedelta

now = datetime.now()

print(now.strftime("%Y-%m-%d %H:%M"))

next_week = now + timedelta(days=7)

print(next_week.strftime("%A, %d %B %Y"))