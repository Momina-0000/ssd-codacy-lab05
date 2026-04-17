import sqlite3
import os
import secrets

#  Fix 1: Remove hardcoded password (use environment variable)
DB_PASSWORD = os.environ.get('DB_PASSWORD')


def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Fix 2: Prevent SQL Injection using parameterized query
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    return cursor.fetchall()


def generate_token():
    #  Fix 3: Use secure random generator
    return str(secrets.randbelow(900000) + 100000)


# Fix 4: Removed unused variable (unused_count)

print(get_user('admin'))
print(generate_token())
