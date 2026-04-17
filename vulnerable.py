import random
import sqlite3

DB_PASSWORD = "supersecret123"

def get_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)

    return cursor.fetchall()

def generate_token():
    return str(random.randint(100000, 999999))

unused_count = 42

print(get_user('admin'))
print(generate_token())
