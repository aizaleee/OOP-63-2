import sqlite3

connect = sqlite3.connect("grades.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject VARCHAR(40) NOT NULL,
        grade INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')
connect.commit()


def create_user(name):
    cursor.execute(f'INSERT INTO users(name) VALUES ("{name}")')
    connect.commit()
    print('Пользователь добавлен!!')

def delete_user(id):
    cursor.execute(f'DELETE FROM users WHERE id = "{id}"')
    connect.commit()
    print('Пользователь удален!!')

# delete_user(2)


def create_grade(subject, grade, user_id):
    cursor.execute(f'INSERT INTO grades(subject, grade, user_id) VALUES ("{subject}", "{grade}", "{user_id}")')
    connect.commit()
    print('Оценка добавлена!!')


# create_user("Oleg")
# create_user("Oleg")
# create_grade("Физре", 5, 3)


def get_user_and_grade():
    cursor.execute('''
        SELECT users.name, grades.subject, grades.grade 
        FROM users FULL OUTER JOIN grades ON users.id = grades.user_id
    ''')
    users = cursor.fetchall()
    for i in users:
        print(f"{i[0]} -- {i[1]} -- {i[2]}")

# get_user_and_grade()


# MAX() MIN() COUNT() SUM() AVG()

def get_agregate():

    cursor.execute('SELECT COUNT(subject) FROM grades')
    data = cursor.fetchone()
    print(data)

# get_agregate()


def create_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS my_view AS
        SELECT name, subject, grade
        FROM users LEFT JOIN grades ON users.id = grades.user_id
        WHERE grade > 4
    ''')
    connect.commit()

# create_view()

def get_view():
    cursor.execute('SELECT * FROM my_view')
    data = cursor.fetchall()
    print(data)

get_view()