
from datetime import datetime

# Take event date and time
event_input = input("Enter event date and time (DD-MM-YYYY HH:MM): ")

# Convert string into datetime object
event_time = datetime.strptime(event_input, "%d-%m-%Y %H:%M")

# Get current date and time
now = datetime.now()

# Check if event has already passed
if event_time < now:
    print("Event has already passed.")

else:
    # Calculate remaining time
    remaining = event_time - now

    # Get total seconds
    total_seconds = int(remaining.total_seconds())

    # Calculate days, hours and minutes
    days = total_seconds // (24 * 60 * 60)

    hours = (total_seconds % (24 * 60 * 60)) // (60 * 60)

    minutes = (total_seconds % (60 * 60)) // 60

    print("\nTime remaining:")
    print("Days:", days)
    print("Hours:", hours)
    print("Minutes:", minutes)