import sqlite3

connect = sqlite3.connect("users.db")
cursor = connect.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            name VARCHAR (50) NOT NULL,
            age INTEGER NOT NULL,
            hobby TEXT
        )
''')
connect.commit()



def create_user(name, age, hobby):
    
    cursor.execute(
        'INSERT INTO users(age, name, hobby) VALUES (?,?,?)',
        (age, name, hobby)
    )
    connect.commit()
    print(f"{name} Создан!!")

# create_user("John", 25, "Наваливать боком!!")
    
def get_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    print(users)

# get_users()

def update_user(ids, name=None, age=None, hobby=None):
    for rowid in ids:
        if name is not None:
            cursor.execute('UPDATE users SET name = ? WHERE rowid = ?', (name, rowid))
        if age is not None:
            cursor.execute('UPDATE users SET age = ? WHERE rowid = ?', (age, rowid))
        if hobby is not None:
            cursor.execute('UPDATE users SET hobby = ? WHERE rowid = ?', (hobby, rowid))
    connect.commit()
    print("updated!")

# update_user([1,2], name="John", hobby="Swimming")
    
def delete_user(ids):
    for rowid in ids:
        cursor.execute(
        'DELETE FROM users WHERE rowid = ?',
        (rowid,)
    )
    connect.commit()
    print('Удалено!!')
# delete_user([2,3])

    




