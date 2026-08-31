#variables & datatype
def variable_and_datatype():
    monthly_income = 50000 #int
    age = 22 #int
    monthly_income_in_float = 50000.00 #float
    name = "Yash" #str
    is_affordable = True # bool
    number = 2 + 3j #complex number

    print(f"monthly_income: {monthly_income},\n{type(monthly_income)}")
    print(f"age is: {age},\n{type(age)}")
    print(f"monthly income in float: {monthly_income_in_float},\n{type(monthly_income_in_float)}")
    print(f"name: {name},\n{type(name)}")
    print(f"is affordable: {is_affordable},\n{type(is_affordable)}")
    print(f"number is: {number},\n{type(number)}")


variable_and_datatype()