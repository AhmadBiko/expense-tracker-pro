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

def get_expenses(user_id):
    with get_connection() as connection:
        with connection.cursor(row_factory=dict_row) as cursor:
            cursor.execute("""SELECT *
            FROM expenses
            WHERE user_id = %s
            ORDER BY date DESC;""",
            (user_id,))
            rows = cursor.fetchall()
    return rows

def add_expense_db(user_id,category, amount, description, date):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute('INSERT INTO expenses(user_id, category, amount, description, date) VALUES(%s,%s,%s,%s,%s) RETURNING id;'
            ,(user_id, category, amount, description, date))
            id = cursor.fetchone()
        return id[0]
            
def update_expense_db(user_id, expense_id, new_amount):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE expenses
            SET amount = %s
            WHERE id = %s AND user_id = %s;""",
            (new_amount, expense_id, user_id))
            result = cursor.rowcount
        return bool(result)

def delete_expense_db(user_id, expense_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""DELETE FROM expenses
            WHERE id = %s AND user_id = %s;""",
            (expense_id, user_id))
            result = cursor.rowcount
        return bool(result)

def get_total_spending_db(user_id):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT COALESCE(SUM(amount), 0) FROM expenses
            WHERE user_id = %s;""",
            (user_id,))
            result = cursor.fetchone()
        return result[0]

def get_monthly_budget(user_id, month):
    with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT amount FROM budgets 
                WHERE month = %s AND user_id = %s""",
                (month, user_id))
                result = cursor.fetchone()
            if result:
                return result[0]
            else:
                return None

def save_monthly_budget(user_id, month, amount):
    with get_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO budgets (user_id, month, amount)
                VALUES (%s, %s, %s)
                ON CONFLICT (user_id, month)
                DO UPDATE SET amount = EXCLUDED.amount;
                """,
                (user_id, month, amount)
            )

def get_monthly_spending(user_id, month):
    with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                """
                SELECT COALESCE(SUM(amount), 0)
                FROM expenses
                WHERE user_id = %s AND TO_CHAR(date, 'YYYY-MM') = %s;
                """,
                (user_id, month))
                result = cursor.fetchone()
            return result[0]

def get_or_create_user(provider, provider_subject, email):
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                """INSERT INTO users (provider, provider_subject, email)
                VALUES (%s, %s, %s)
                ON CONFLICT (provider, provider_subject)
                DO UPDATE SET email = EXCLUDED.email
                RETURNING id;""",
                (provider, provider_subject, email))
                user = cursor.fetchone()
            return user[0]