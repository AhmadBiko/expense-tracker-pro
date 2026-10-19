import json
from datetime import date

#[1] Creating add function
def add_expense(expenses, category, amount, description):
    # making sure that only valid data goes to the process
    if isinstance(amount, bool):
        raise TypeError('Amount must be a number !')
    if not isinstance(amount, (float, int)):
        raise TypeError('Amount must be a number !')
    elif amount <= 0:
        raise ValueError('Amount must be positive !')
    if not category.strip():
        raise ValueError('Category can\'t be empty !')
    if not description.strip():
        raise ValueError('Description can\'t be empty !')
    data = {}
    data["category"] = category.strip()
    data["amount"] = amount
    data["description"] = description.strip()
    data["date"] = date.today().isoformat()
    expenses.append(data)

#[2] Creating sum function
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

#[3] Creating specific sum function
def calculate_category_total(expenses, category):
    is_found = False
    total  = 0 
    for expense in expenses:
        if expense["category"] == category:
            is_found = True
            total += expense["amount"]
    if is_found:
        return total
    else:
        return 0

#[4] Creating most expensive function
def find_most_expensive(expenses):
    if not expenses:
        return None
    most_expensive = expenses[0]["amount"]
    most_expensive_expense = expenses[0]
    for  expense in expenses:
        if expense["amount"] > most_expensive:
            most_expensive = expense["amount"]
            most_expensive_expense = expense
    return most_expensive_expense

#[5] Creating delete function
def delete_expense(expenses, selection):
    if isinstance(selection, bool):
        raise TypeError(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
    if not isinstance(selection, int):
        raise TypeError(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
    if selection < 1 or selection > len(expenses):
        raise ValueError(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
    expenses.pop(selection - 1)
    return 'Expense deleted successfully!\n' 

#[6] Creating saving data function
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

#[7] Creating loading data function
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('Error: expenses.json contains invalid JSON. Your data has not been modified.') 
        raise

#[8] Creating saving budget function
def save_budget(budget):
    with open("budget.json", "w") as file:
        json.dump({"budget": budget}, file)

#[9] Creating loading budget function
def load_budget():
    try:
        with open("budget.json", "r") as file:
            data = json.load(file)
            return data["budget"]
    except FileNotFoundError:
        return 300.0
    except json.JSONDecodeError:
        print('Error: budget.json contains invalid JSON. Your data has not been modified.')
        raise

#[10] Creating monthly total function
def calculate_monthly_total(expenses):
    current_month = date.today().isoformat()[:7]
    total = 0
    for expense in expenses:
        if expense.get("date", "")[:7] == current_month :
            total += expense["amount"]
    return total

#[11] Creating spent per month function
def calculate_spending_by_month(expenses):
    monthly_list = {}
    for expense in expenses:
        if "date" in expense:
            month = expense["date"][:7]
            if month in monthly_list:
                monthly_list[month] += expense["amount"]
            else:
                monthly_list[month] = expense["amount"]
    return monthly_list