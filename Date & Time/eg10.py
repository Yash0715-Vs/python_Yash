from datetime import datetime, timedelta

# Take joining date
joining_input = input("Enter joining date (DD-MM-YYYY): ")
joining_date = datetime.strptime(joining_input, "%d-%m-%Y")

# Take leave start date
leave_input = input("Enter leave start date (DD-MM-YYYY): ")
leave_start = datetime.strptime(leave_input, "%d-%m-%Y")

# Calculate days worked before leave
days_worked = leave_start - joining_date

# Take number of leave days
leave_days = int(input("Enter number of leave days: "))

# Calculate leave end date
leave_end = leave_start + timedelta(days=leave_days)

print("\n details:")
print("Joining Date:",
      joining_date.strftime("%d-%B-%Y"))

print("Leave Starts:",
      leave_start.strftime("%d-%B-%Y"))

print("Days Worked:", days_worked.days)

print("Leave Ends:",
      leave_end.strftime("%d-%B-%Y"))
