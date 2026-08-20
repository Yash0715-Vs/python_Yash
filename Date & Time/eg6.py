from datetime import datetime

date_string = input("Enter date (DD-MM-YYYY): ")

date = datetime.strptime(date_string, "%d-%m-%Y")

print("Date:", date)