import sqlite3

connect = sqlite3.connect("restaurant.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL
    
)
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    dish TEXT NOT NULL,
    price INTEGER NOT NULL,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
)
''')
connect.commit()

def create_client(name):
    cursor.execute(f'INSERT INTO Clients(name) VALUES ("{name}")')
    connect.commit()
    print('CLient been added')


def create_order(client_id, dish, price):
    cursor.execute(f'INSERT INTO Orders (client_id, dish, price) VALUES ("{client_id}", "{dish}","{price}")')
    connect.commit()
    print('Order been added')


# create_client('Aiz')
# create_client('Papa')
# create_client('Oleg')
# create_order(2, 'Pasta', 100)
# create_order(3, 'Soup', 60)
# create_order(1, 'Steak', 555 )
    
def create_view():
    cursor.execute('''
        CREATE VIEW IF NOT EXISTS total_view AS
        SELECT Clients.name AS ClientName,
            COUNT(Orders.order_id) AS TotalOrders, SUM(Orders.price) AS TotalSpent
        FROM Orders  JOIN Clients ON Orders.client_id = Clients.client_id
        GROUP BY Clients.client_id;
    ''')
    connect.commit()
    print('worked')
create_view()

def get_view():
    cursor.execute('SELECT * FROM total_view')
    data = cursor.fetchall()
    print(data)
    print('worked2')

get_view()