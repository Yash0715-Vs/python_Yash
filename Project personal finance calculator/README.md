# Personal Finance Calculator

## 1. Project Description

The Personal Finance Calculator is a Python program that helps a user understand their monthly financial situation.

The program accepts the user's name, monthly income, and different monthly expenses. It then calculates total expenses, savings, savings percentage, and determines whether the expenses are affordable.

This project demonstrates Python fundamentals including variables, data types, input/output, operators, type conversion, exception handling, functions, and formatted output.

---

## 2. Features

The program provides the following features:

* Accepts user input.
* Converts numeric input into `float`.
* Validates numeric input.
* Prevents negative income and expenses.
* Calculates total expenses.
* Calculates total savings.
* Calculates savings percentage.
* Determines affordability.
* Displays a formatted financial report.
* Demonstrates Python data types.
* Demonstrates different Python operators.

---

## 3. Python Concepts Used

### Data Types

The program demonstrates:

* `int`
* `float`
* `str`
* `bool`
* `complex`

### Operators

The program demonstrates:

* Arithmetic operators
* Comparison operators
* Logical operators
* Assignment operators
* Identity operators
* Membership operators
* Bitwise operators

---

## 4. Program Flow

The program follows these steps:

1. Demonstrate the required Python data types.
2. Demonstrate the required operators.
3. Ask the user for their name.
4. Ask for monthly income.
5. Ask for different monthly expenses.
6. Validate all numeric inputs.
7. Calculate total expenses.
8. Calculate savings.
9. Calculate savings percentage.
10. Check affordability.
11. Display the final financial report.

---

## 5. Calculations

### Total Expenses

```text
Total Expenses =
Rent + Food + Transport + Utilities + Entertainment
```

### Savings

```text
Savings =
Monthly Income - Total Expenses
```

### Savings Percentage

```text
Savings Percentage =
(Savings / Monthly Income) × 100
```

If monthly income is zero, the savings percentage is set to zero to avoid division by zero.

### Affordability

```text
If Total Expenses <= Monthly Income
    Affordable
Else
    Not Affordable
```

---

## 6. Input Validation

The program handles invalid numeric input using `try` and `except`.

For example, if the user enters:

```text
Enter your monthly income: abc
```

The program displays:

```text
Invalid input. Please enter a number.
```

The program then asks the user to enter the value again.

The program also prevents negative values.

Example:

```text
Enter your monthly income: -5000
Please enter a non-negative number.
```

The user is asked to enter the value again.

---

## 7. Sample Input

```text
Enter your name: Yash
Enter your monthly income: ₹50000

Enter your monthly expenses:
Rent: ₹15000
Food: ₹5000
Transport: ₹3000
Utilities: ₹2000
Entertainment: ₹2000
```

## 8. Sample Output

```text
==================================================
             PERSONAL FINANCE REPORT
==================================================

Name           : Yash
Monthly Income : ₹50,000.00

EXPENSES
--------------------------------------------------
Rent              : ₹15,000.00
Food              : ₹5,000.00
Transport         : ₹3,000.00
Utilities         : ₹2,000.00
Entertainment     : ₹2,000.00
--------------------------------------------------
Total Expenses     : ₹27,000.00

FINANCIAL SUMMARY
--------------------------------------------------
Savings            : ₹23,000.00
Savings Percentage : 46.00%
Affordability      : Affordable
==================================================
```

---

## 9. Error and Edge-Case Testing

### Test Case 1 — Valid Input

Input:

```text
Income = 50000
Expenses = 27000
```

Expected result:

```text
Savings = ₹23000
Savings Percentage = 46%
Affordability = Affordable
```

---

### Test Case 2 — Invalid Text Input

Input:

```text
abc
```

Expected result:

```text
Invalid input. Please enter a number.
```

The program does not crash.

---

### Test Case 3 — Negative Input

Input:

```text
-5000
```

Expected result:

```text
Please enter a non-negative number.
```

The program asks for the value again.

---

### Test Case 4 — Expenses Greater Than Income

Input:

```text
Income = 20000
Expenses = 25000
```

Expected result:

```text
Savings = -₹5000
Affordability = Not Affordable
```

---

### Test Case 5 — Zero Income

Input:

```text
Income = 0
```

The program avoids division by zero and sets:

```text
Savings Percentage = 0%
```

---

## 10. Design Decisions

### Functions

The program is divided into separate functions:

* `get_positive_number()` handles input validation.
* `demonstrate_data_types()` demonstrates required data types.
* `demonstrate_operators()` demonstrates required operators.
* `calculate_finance()` handles financial calculations.
* `display_report()` handles formatted output.
* `main()` controls the overall program flow.

This keeps each function focused on one responsibility.

### Dictionary for Expenses

A dictionary is used to store expense categories and their amounts:

```python
expenses = {
    "Rent": 15000,
    "Food": 5000,
    "Transport": 3000,
    "Utilities": 2000,
    "Entertainment": 2000
}
```

This makes the expenses easy to manage and allows the total to be calculated using:

```python
sum(expenses.values())
```

### Exception Handling

`try` and `except ValueError` are used to prevent invalid numeric input from crashing the program.

### Formatted Output

f-strings are used to make the final report readable and to format money values with commas and two decimal places.

---

## 11. Code Quality

The final program follows the assignment's coding standards by:

* Using meaningful variable names.
* Using focused functions.
* Avoiding unnecessary duplication.
* Validating user input.
* Handling expected errors.
* Using comments/docstrings where useful.
* Keeping formatting consistent.
* Separating calculations from presentation.

---

## 12. How to Run

Make sure Python is installed on the computer.

Save the program as:

```text
main.py
```

Open a terminal in the project folder and run:

```bash
python main.py
```

The program will start and ask for the user's information.

---

## 13. Conclusion

This project demonstrates how a real-world problem can be broken down into smaller programming tasks.

The Personal Finance Calculator uses Python fundamentals to collect information, process data, perform calculations, validate input, and present the results in a clear format.

The project covers the required concepts from the Python Problem-Solving Foundations assignment.
