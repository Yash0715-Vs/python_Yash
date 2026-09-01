# Personal Finance Calculator

## 1. Project Description

A simple Python program that helps users track their income and expenses and calculate their financial status.

## 2. Features

* Enter user's name.
* Add up to 10 income sources.
* Add up to 10 expenses.
* Enter category and amount for each entry.
* Calculate total income and expenses.
* Calculate savings.
* Calculate percentage saved.
* Check affordability.
* Validate numeric input.
* Save entered data in a JSON file.(THIS IS AN EXTRA FEATURE WHICH I HAVE ADD BY MY SELF)

## 3. Technologies

* Python 3
* Lists
* Dictionaries
* Loops
* Functions
* Conditional statements
* Exception handling
* JSON

## 4. Main Calculations

```text
Total Income = Sum of all incomes

Total Expenses = Sum of all expenses

Savings = Total Income - Total Expenses

Percent Saved = (Savings / Total Income) × 100

Affordable = Total Expenses <= Total Income
```

## 5. Input Validation

* Invalid numbers are rejected.
* Zero and negative amounts are rejected.
* `try-except` prevents the program from crashing.

## 6. Data Storage

Income and expenses are stored as lists of dictionaries:

```python
{
    "category": "Salary",
    "amount": 50000
}
```

The entered data is saved automatically in:

```text
finance_data.json
```

Example:

```json
{
    "name": "Yash",
    "income": [
        {
            "category": "Salary",
            "amount": 50000
        }
    ],
    "expenses": [
        {
            "category": "Rent",
            "amount": 15000
        }
    ]
}
```

JSON is used to store the user's entered financial data in a structured format.

## 7. Sample Output

```text
==================================================
             PERSONAL FINANCE REPORT
==================================================
Name: Yash

Income:
Salary : ₹ 50000.0

Expenses:
Rent : ₹ 15000.0

==================================================
Total Income: ₹50000.0
Total Expenses: ₹15000.0
Savings: ₹35000.0
Percent Saved: 70.00%
Affordable: Yes
```

The program also displays:

```text
Data saved successfully to finance_data.json
```

## 8. How to Run

Save the files as:

```text
Personal_Finance_Calculator/
│
├── main1.py
├── finance_data.json
└── README.md
```

Run the program using:

```bash
python main1.py
```

`finance_data.json` will be created automatically after entering the data.

## 9. Limitations

* Maximum 10 income entries.
* Maximum 10 expense entries.
* Categories are entered manually.
* JSON data is overwritten when the program is run again.
* No database is used.

## 10. Future Improvements

* Keep previous financial records instead of overwriting them.
* Add predefined categories using JSON.
* Add monthly financial tracking.
* Add graphs and reports.
* Add editing and deleting of financial records.
