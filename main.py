#[1] Importing the needed functions
import json
import time
import sys
from expense_functions import (
    add_expense,
    calculate_total,
    calculate_category_total,
    find_most_expensive,
    delete_expense,
    save_expenses,
    load_expenses
)

#[2] Loading the data
try:
    expenses = load_expenses()
    time.sleep(0.5)
    print("Loading your expenses...\n")
    time.sleep(1)
except json.JSONDecodeError:
    print('Error: Could not load saved expenses.')
    time.sleep(1)
    print('Please check expenses.json.')
    time.sleep(1)
    print('Application stopped to protect your data.')
    sys.exit(1)
    
    
    

#[3] Creating my main menu
app = '===== Expense Tracker Pro =====\n'
main_menu = '1. Add expense\n'
main_menu += '2. Show all expenses\n'
main_menu += '3. Show total spending\n'
main_menu += '4. Show spending by category\n'
main_menu += '5. Show most expensive expense\n'
main_menu += '6. Delete an expense\n'
main_menu += '7. Exit\n'

#[4] Starting the app
print("Ready! 🚀\n")
print(app)
while True:
    print(main_menu)
    try:
        user_input = int(input())
    except ValueError:
        print('Please enter a valid number !\n')
    else :
        if user_input == 1:
            category = input('Enter a category:').title()
            try:
                amount = float(input('Enter an amount:'))
            except ValueError:
                print('Please enter a valid number !')
                continue
            else:
                description = input('Enter a description:')
            try:
                add_expense(expenses, category, amount, description)
            except ValueError:
                print('Please give a name for your category and description and a positive number !\n')
            except TypeError:
                print('Please enter a number !\n')
            else:
                save_expenses(expenses)
                print("Adding expense...")
                time.sleep(1)
                print('Expense added successfully!\n')
        elif user_input == 2:
            if not expenses:
                print('There is no expenses yet !\n')
            else:
                print("Loading expenses...\n")
                for expense in expenses:
                    print(f'{expense["category"]} | {expense["amount"]:.2f} € | {expense["description"]}')
                    time.sleep(0.5)
        elif user_input == 3:
            print(f'Total spent: {calculate_total(expenses):.2f} €')
        elif user_input == 4:
            search = input('Enter a category:').title()
            print(f'Total spending for {search}: {calculate_category_total(expenses, search):.2f} €')
        elif user_input == 5:
            data = find_most_expensive(expenses)
            if not data:
                print('No expenses recorded yet.\n')      
            else:
                print('Finding most expensive expense...\n')
                time.sleep(1)
                print(f'{data["category"]} | {data["amount"]:.2f} € | {data["description"]}')
        elif user_input == 6:
            if not expenses:
                print('There is no expenses to delete !\n')
                continue
            print('Select an expense to delete:\n')
            for index, expense in enumerate(expenses, 1):
                print(f'{index}. {expense["category"]} | {expense["amount"]:.2f} € | {expense["description"]}\n')
                time.sleep(0.5)
            while True:
                try:
                    del_option = int(input('Enter the expense number:\n'))
                except ValueError:
                    print(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
                    continue
                else: 
                    if del_option < 1:
                        print(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
                        continue
                    elif del_option > len(expenses):
                        print(f'Invalid selection. Please choose a number between 1 and {len(expenses)}\n')
                        continue
                    else:
                        print('Deleting expense...\n')
                        time.sleep(1)
                        break
            print(delete_expense(expenses, del_option))
            save_expenses(expenses)
        elif user_input == 7:
            break
        else:
            print('Please choose a number between 1 to 7 !\n')