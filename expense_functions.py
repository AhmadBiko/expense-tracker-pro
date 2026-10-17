import json

#[1] creating add function
def add_expense(expenses, category, amount, description):
    # making sure that only valid data goes to the process
    if isinstance(amount, bool):
        raise TypeError('amount must be a number !')
    if not isinstance(amount, (float, int)):
        raise TypeError('amount must be a number !')
    elif amount <= 0:
        raise ValueError('amount must be positive !')
    if not category.strip():
        raise ValueError('category can\'t be empty !')
    if not description.strip():
        raise ValueError('description can\'t be empty !')
    data = {}
    data["category"] = category.strip()
    data["amount"] = amount
    data["description"] = description.strip()
    expenses.append(data)

#[2] creating sum function
def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    return total

#[3] creating specific sum function
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

#[4] creating most expensive function
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

#[5] creating delete function
def delete_expense(expenses, selection):
    if isinstance(selection, bool):
        raise TypeError(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
    if not isinstance(selection, int):
        raise TypeError(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
    if selection < 1 or selection > len(expenses):
        raise ValueError(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
    expenses.pop(selection - 1)
    return 'Expense deleted successfully!\n' 

#[6] creating saving data function
def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

#[7] creating loading data function
def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file) 
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('Error: expenses.json contains invalid JSON. Your data has not been modified.') 
        raise