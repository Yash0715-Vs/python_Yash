def calculate_total(marks):
    # Base case
    if len(marks) == 0:
        return 0

    # Recursive case
    return marks[0] + calculate_total(marks[1:])


def report_card(name, *marks, **details):

    # Add 5 grace marks to every subject
    grace_marks = list(map(lambda mark: mark + 5, marks))

    # Calculate total using recursion
    total = calculate_total(grace_marks)

    # Calculate average
    average = total / len(grace_marks)

    # Highest and lowest using lambda
    highest = max(grace_marks, key=lambda x: x)
    lowest = min(grace_marks, key=lambda x: x)

    # Sort marks using lambda
    sorted_marks = sorted(grace_marks, key=lambda x: x)

    # Count passing marks (40 or above)
    passing_marks = list(filter(lambda mark: mark >= 40, grace_marks))

    # Grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "Fail"

    # Pass/Fail
    if len(passing_marks) == len(grace_marks):
        result = "Pass"
    else:
        result = "Fail"

    # Print Report
    print("\n========== REPORT CARD ==========")
    print(f"Student Name : {name}")
    print(f"Roll Number  : {details['roll_number']}")
    print(f"Department   : {details['department']}")
    print(f"Phone        : {details['phone']}")
    print(f"City         : {details['city']}")
    print(f"Marks        : {grace_marks}")
    print(f"Total        : {total}")
    print(f"Average      : {average:.2f}")
    print(f"Highest      : {highest}")
    print(f"Lowest       : {lowest}")
    print(f"Grade        : {grade}")
    print(f"Pass/Fail    : {result}")
    print(f"Sorted Marks : {sorted_marks}")

    # Return report as dictionary
    report = {
        "name": name,
        "roll_number": details['roll_number'],
        "department": details['department'],
        "phone": details['phone'],
        "city": details['city'],
        "marks": grace_marks,
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "grade": grade,
        "result": result
    }

    return report


# Function Call
report = report_card(
    "Yash",
    85, 90, 78, 88, 95,
    roll_number=101,
    department="Computer",
    phone="9876543210",
    city="Ahmedabad"
)

print("\nReturned Dictionary:")
print(report)