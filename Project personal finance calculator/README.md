# Personal Finance Calculator

## 1. Project Description

The **Personal Finance Calculator** is a simple Python program that helps users track their income and expenses.

The program allows the user to:

* Enter their name.
* Add multiple income sources.
* Add multiple expenses.
* Enter a category for each income and expense.
* Calculate total income.
* Calculate total expenses.
* Calculate savings.
* Calculate the percentage of income saved.
* Check whether the expenses are affordable based on the total income.

The program allows a maximum of **10 income entries** and **10 expense entries**.

---

## 2. Features

### Income Management

The user can enter:

* Income category
* Income amount

The user can choose whether to add another income using:

```text
(y/n)
```

Example:

```text
Enter income category: Salary
Enter income amount: 50000
Do you want to add another income? (y/n): y

Enter income category: Freelancing
Enter income amount: 10000
Do you want to add another income? (y/n): n
```

---

### Expense Management

The user can enter:

* Expense category
* Expense amount

The user can also choose whether to add another expense.

Example:

```text
Enter expense category: Rent
Enter expense amount: 15000
Do you want to add another expense? (y/n): y

Enter expense category: Food
Enter expense amount: 5000
Do you want to add another expense? (y/n): n
```

---

## 3. Technologies Used

* **Python 3**
* Python built-in functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* Functions
* Exception handling
* Formatted strings

No external libraries are required.

---

## 4. Program Structure

The program contains two main functions:

### `get_amount()`

This function gets a valid positive number from the user.

It uses:

```python
try:
    value = float(input(message))
```

If the user enters invalid text, the program displays:

```text
Invalid input. Please enter a number.
```

It also prevents zero and negative values:

```python
if value <= 0:
    print("Please enter a positive number.")
```

---

### `main()`

The `main()` function controls the complete program.

It:

1. Gets the user's name.
2. Collects income information.
3. Collects expense information.
4. Calculates total income.
5. Calculates total expenses.
6. Calculates savings.
7. Calculates percentage saved.
8. Checks affordability.
9. Displays the final report.

---

## 5. Data Storage

Income and expenses are stored using lists containing dictionaries.

### Income

Example:

```python
income = [
    {
        "category": "Salary",
        "amount": 50000
    },
    {
        "category": "Freelancing",
        "amount": 10000
    }
]
```

### Expenses

Example:

```python
expenses = [
    {
        "category": "Rent",
        "amount": 15000
    },
    {
        "category": "Food",
        "amount": 5000
    }
]
```

Using a dictionary allows both the **category** and **amount** to be stored together.

---

## 6. Calculations

### Total Income

The program loops through all income entries and adds their amounts.

```python
total_income = 0

for item in income:
    total_income += item["amount"]
```

---

### Total Expenses

The program loops through all expense entries and adds their amounts.

```python
total_expenses = 0

for item in expenses:
    total_expenses += item["amount"]
```

---

### Savings

Savings are calculated using:

```text
Savings = Total Income - Total Expenses
```

Python:

```python
savings = total_income - total_expenses
```

---

### Percentage Saved

The percentage of income saved is calculated using:

```text
Percentage Saved =
(Savings / Total Income) × 100
```

Python:

```python
percent_saved = savings / total_income * 100
```

If the total income is zero, the program sets the percentage saved to zero to avoid division by zero.

---

### Affordability

The program checks whether total expenses are less than or equal to total income.

```python
if total_expenses <= total_income:
    print("Affordable: Yes")
else:
    print("Affordable: No")
```

If:

```text
Total Expenses <= Total Income
```

the result is:

```text
Affordable: Yes
```

Otherwise:

```text
Affordable: No
```

---

## 7. Input Validation

The program validates the amount entered by the user.

### Invalid Number

If the user enters:

```text
abc
```

the program displays:

```text
Invalid input. Please enter a number.
```

---

### Zero or Negative Number

If the user enters:

```text
-5000
```

or:

```text
0
```

the program displays:

```text
Please enter a positive number.
```

The user is then asked to enter the amount again.

---

## 8. Sample Input

```text
=== Personal Finance Calculator ===
Enter your name: Yash

--- INCOME ---
Enter income category: Salary
Enter income amount: 50000
Do you want to add another income? (y/n): y

Enter income category: Freelancing
Enter income amount: 10000
Do you want to add another income? (y/n): n

--- EXPENSES ---
Enter expense category: Rent
Enter expense amount: 15000
Do you want to add another expense? (y/n): y

Enter expense category: Food
Enter expense amount: 5000
Do you want to add another expense? (y/n): y

Enter expense category: Transport
Enter expense amount: 3000
Do you want to add another expense? (y/n): n
```

---

## 9. Sample Output

```text
==================================================
             PERSONAL FINANCE REPORT
==================================================
Name: Yash

Income:
Salary : ₹ 50000.0
Freelancing : ₹ 10000.0

Expenses:
Rent : ₹ 15000.0
Food : ₹ 5000.0
Transport : ₹ 3000.0

==================================================
Total Income: ₹60000.0
Total Expenses: ₹23000.0
Savings: ₹37000.0
Percent Saved: 61.67%
Affordable: Yes
```

---

## 10. Test Cases

| Test Case                 | Input                            | Expected Result               |
| ------------------------- | -------------------------------- | ----------------------------- |
| Valid income and expenses | Income = 60000, Expenses = 23000 | Savings = 37000               |
| Multiple incomes          | 50000 + 10000                    | Total Income = 60000          |
| Multiple expenses         | 15000 + 5000 + 3000              | Total Expenses = 23000        |
| Invalid amount            | `abc`                            | Shows invalid input message   |
| Negative amount           | `-5000`                          | Shows positive number message |
| Zero amount               | `0`                              | Shows positive number message |
| Expenses below income     | Income > Expenses                | Affordable: Yes               |
| Expenses above income     | Income < Expenses                | Affordable: No                |
| Maximum entries           | 10 incomes/expenses              | Program accepts entries       |
| Zero total income         | Income = 0                       | Percentage Saved = 0          |

