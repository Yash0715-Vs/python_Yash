import pandas as pd

data = {
    "Name": ["Yash", "Rahul", "Amit", "Neha", "Priya"],
    "DaysPresent": [85, 72, 90, 65, 78],
    "TotalDays": [100, 100, 100, 100, 100]
}

df = pd.DataFrame(data)

# 1. Add AttendancePercentage column
df["AttendancePercentage"] = (
    df["DaysPresent"] / df["TotalDays"]
) * 100

print("Student Attendance:")
print(df)


# 2. Students with attendance >= 75%
print(f"\nStudents with attendance >= 75%: \n{df[df["AttendancePercentage"] >= 75]}")

# 3. Students below 75%
print(f"\nStudents below 75%: \n{df[df["AttendancePercentage"] < 75]}")

# 4. Highest attendance
print(f"\nHighest Attendance: \n{df['AttendancePercentage'].max()}%")

# 5. Lowest attendance
print(f"Lowest Attendance: \n{df['AttendancePercentage'].min()}%")

# 6. Average attendance
print(f"Average Attendance: \n{df['AttendancePercentage'].mean()}%")


# 7. Add Status column
df["Status"] = df["AttendancePercentage"].apply(
    lambda x: "Eligible" if x >= 75 else "Not Eligible"
)

print("\nStatus:")
print(df[["Name", "AttendancePercentage", "Status"]])


# Save old status before adding 5 days
old_status = df["Status"].copy()


# 8. Every student attends 5 more days
df["DaysPresent"] = df["DaysPresent"] + 5
df["TotalDays"] = df["TotalDays"] + 5


# 9. Recalculate percentage
df["AttendancePercentage"] = (
    df["DaysPresent"] / df["TotalDays"]
) * 100

# Update Status
df["Status"] = df["AttendancePercentage"].apply(
    lambda x: "Eligible" if x >= 75 else "Not Eligible"
)

print("\nAfter attending 5 more days:")
print(df)


# 10. Students who became eligible
print("\nStudents who became eligible after 5 more days:")

became_eligible = df[
    (old_status == "Not Eligible") &
    (df["Status"] == "Eligible")
]

for name, percentage in zip(
    became_eligible["Name"],
    became_eligible["AttendancePercentage"]
):
    print(
        f"{name} is now eligible "
        f"with {percentage:.2f}% attendance."
    )