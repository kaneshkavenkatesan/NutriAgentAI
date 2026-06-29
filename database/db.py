import sqlite3


def create_table():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        age INTEGER,
        gender TEXT,
        height REAL,
        weight REAL,
        goal TEXT,
        food_preference TEXT,
        bmi REAL,
        status TEXT,
        calories INTEGER
    )
    """)

    conn.commit()
    conn.close()


def save_user(
    name,
    email,
    age,
    gender,
    height,
    weight,
    goal,
    food_preference,
    bmi,
    status,
    calories
):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (
        name,
        email,
        age,
        gender,
        height,
        weight,
        goal,
        food_preference,
        bmi,
        status,
        calories
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    """,
    (
        name,
        email,
        age,
        gender,
        height,
        weight,
        goal,
        food_preference,
        bmi,
        status,
        calories
    ))

    conn.commit()
    conn.close()


def get_users():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")

    users = cursor.fetchall()

    conn.close()

    return users

def delete_user(user_id):

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()
def get_latest_user():

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM users
    ORDER BY id DESC
    LIMIT 1
    """)

    user = cursor.fetchone()

    conn.close()

    return user