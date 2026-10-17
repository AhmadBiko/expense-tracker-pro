#[1] importing the needed functions
import unittest
from expense_functions import (
    add_expense,
    calculate_total,
    calculate_category_total,
    find_most_expensive,
    delete_expense
)

#[2] starting our tests
class TestExpenseFunctions(unittest.TestCase):

    def setUp(self):
        self.expenses = [
            {"category": "Food", "amount": 25.50, "description": "Groceries"},
            {"category": "Transport", "amount": 15.00, "description": "Ticket"}
        ]

    def test_setUp_creates_two_expenses(self):
        self.assertEqual(len(self.expenses), 2)

    def test_add_expense(self):
        expenses = []
        add_expense(expenses, 'Food', 25.50, 'Groceries')
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["category"], 'Food')
        self.assertEqual(expenses[0]["amount"], 25.50)
        self.assertEqual(expenses[0]["description"], 'Groceries')

    def test_add_expense_negative_amount(self):
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, 'Food', -5, 'Groceries')
        self.assertEqual(expenses, [])

    def test_add_expense_zero_amount(self):
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, 'Food', 0, 'Groceries')
        self.assertEqual(expenses, [])

    def test_add_expense_invalid_amount_type(self):
        expenses = []
        with self.assertRaises(TypeError):
            add_expense(expenses, 'Food', 'twenty', 'Groceries')
        with self.assertRaises(TypeError):
            add_expense(expenses, 'Food', True, 'Groceries')
        self.assertEqual(expenses, [])

    def test_add_expense_invalid_category(self):
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, '', 25.50, 'Groceries')
        with self.assertRaises(ValueError):
            add_expense(expenses, '   ', 25.50, 'Groceries')
        self.assertEqual(expenses, [])

    def test_add_expense_invalid_description(self):
        expenses = []
        with self.assertRaises(ValueError):
            add_expense(expenses, 'Food', 25.50, '')
        with self.assertRaises(ValueError):
            add_expense(expenses, 'Food', 25.50, '    ')
        self.assertEqual(expenses, [])

    def test_add_expense_strips_whitespace(self):
        expenses = []
        add_expense(expenses, '  Food  ', 25.50, '  Groceries  ')
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["category"], 'Food')
        self.assertEqual(expenses[0]["amount"], 25.50)
        self.assertEqual(expenses[0]["description"], 'Groceries')

    def test_calculate_total(self):
        result = calculate_total(self.expenses)
        self.assertEqual(result, 40.50)

    def test_calculate_total_single_expense(self):
        expenses = [
            {"category": "Food", "amount": 12.50, "description": "Lunch"}
        ]
        result = calculate_total(expenses)
        self.assertEqual(result, 12.50)

    def test_calculate_category_total(self):
        expenses = [
            {"category": "Food", "amount": 25.50, "description": "Groceries"},
            {"category": "Transport", "amount": 15.00, "description": "Monthly ticket"},
            {"category": "Food", "amount": 12.00, "description": "Lunch"}
        ]
        result_1 = calculate_category_total(expenses, 'Food')
        result_2 = calculate_category_total(expenses, 'Transport')
        result_3 = calculate_category_total(expenses, 'Entertainment')
        self.assertEqual(result_1, 37.50)
        self.assertEqual(result_2, 15.00)
        self.assertEqual(result_3, 0.00)

    def test_find_most_expensive(self):
        expenses = []
        result_1 = find_most_expensive(expenses)
        self.assertIsNone(result_1)
        expenses = [
            {"category": "Food", "amount": 25.50, "description": "Groceries"},
            {"category": "Transport", "amount": 15.00, "description": "Monthly ticket"},
            {"category": "Food", "amount": 12.00, "description": "Lunch"},
        ]
        result_2 = find_most_expensive(expenses)
        self.assertEqual(result_2, expenses[0])
        expenses = [
            {"category": "Food", "amount": 12.00, "description": "Lunch"},
            {"category": "Drink", "amount": 12.00, "description": "Coffee"}
        ]
        result_3 = find_most_expensive(expenses)
        self.assertEqual(result_3, expenses[0])
        
    def test_delete_expense(self):
        result = delete_expense(self.expenses, 1)
        self.assertEqual(len(self.expenses), 1)
        self.assertEqual(self.expenses[0]["category"], 'Transport')
        self.assertEqual(result, "Expense deleted successfully!\n")
        

    def test_delete_only_expense(self):
        expenses =[ {"category": "Food", "amount": 25.50, "description": "Groceries"} ]
        delete_expense(expenses, 1)
        self.assertEqual(expenses, [])

    def test_delete_expense_invalid_selection(self):
        with self.assertRaises(ValueError):
            delete_expense(self.expenses, 5)
        self.assertEqual(len(self.expenses), 2)

    def test_delete_expense_invalid_type(self):
        original_expenses = self.expenses.copy()
        cases = [
            ("hello", TypeError),
            (1.5, TypeError),
            (True, TypeError)
        ]
        for selection, expected_exception in cases:
            with self.subTest(selection=selection):
                with self.assertRaises(expected_exception):
                    delete_expense(self.expenses, selection)
        self.assertEqual(original_expenses, self.expenses)

    def test_delete_expense_negative_selection(self):
        original_expenses = self.expenses.copy()
        with self.assertRaises(ValueError):
            delete_expense(self.expenses, -1)
        self.assertEqual(original_expenses, self.expenses)

    def test_delete_expense_last_selection(self):
        delete_expense(self.expenses, 2)
        self.assertEqual(len(self.expenses), 1)
        self.assertEqual(self.expenses[0]["category"], 'Food')

if __name__ == "__main__":
    unittest.main()