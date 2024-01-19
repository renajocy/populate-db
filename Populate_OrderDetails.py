from faker import Faker
import mysql.connector
import random

fake = Faker()

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cafeteria'
)
cursor = conn.cursor()

order_id_range = range(1, 2007)
item_id_range = range(1, 2002)

for _ in range(2000):
    order_id = random.choice(order_id_range)
    item_id = random.choice(item_id_range)
    quantity = random.randint(1, 10)
    price = round(random.uniform(1, 100), 2)

    query = """
    INSERT INTO orderdetails (OrderID, ItemID, Quantity, Price) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (order_id, item_id, quantity, price))

conn.commit()
cursor.close()
conn.close()
