import psycopg
from psycopg.rows import dict_row
import os

def get_connection():
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        return psycopg.connect(database_url)
    else:
        return psycopg.connect(
            dbname="expense_tracker",
            user="postgres",
            password=os.environ["DB_PASSWORD"],
            host="localhost",
            port=5432
        )

def get_expenses():
    with get_connection() as connection:
        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute("SELECT * FROM expenses;")
            rows = cursor.fetchall()
    return rows

def add_expense_db(category, amount, description, date):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO expenses(category, amount, description, date) VALUES(%s,%s,%s,%s) RETURNING id;'
            ,(category, amount, description, date))
            id = cursor.fetchone()
        return id[0]
            
def update_expense_db(expense_id, new_amount):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('UPDATE expenses SET amount = %s WHERE id = %s;',
            (new_amount, expense_id))
            result = cursor.rowcount
        return bool(result)

def delete_expense_db(expense_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('DELETE FROM expenses WHERE id = %s',
            (expense_id,))
            result = cursor.rowcount
        return bool(result)

def get_total_spending_db():
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('SELECT COALESCE(SUM(amount), 0) FROM expenses;')
            result = cursor.fetchone()
        return result[0]

def get_monthly_budget(month):
    with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT amount FROM budgets WHERE month = %s",
                (month,))
                result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None

def save_monthly_budget(month, amount):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO budgets (month, amount)
                VALUES (%s, %s)
                ON CONFLICT (month)
                DO UPDATE SET amount = EXCLUDED.amount;
                """,
                (month, amount)
            )

def get_monthly_spending(month):
    with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                """
                SELECT COALESCE(SUM(amount), 0)
                FROM expenses
                WHERE TO_CHAR(date, 'YYYY-MM') = %s;
                """,
                (month,))
                result = cursor.fetchone()
            return result[0]

if __name__ == "__main__":
    save_monthly_budget("2026-11", 200)
    print(get_monthly_budget("2026-11"))

    save_monthly_budget("2026-11", 350)
    print(get_monthly_budget("2026-11"))