from faker import Faker
import mysql.connector
import random
from datetime import datetime, timedelta

fake = Faker()

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cafeteria'
)
cursor = conn.cursor()

start_date = datetime.today() - timedelta(days=365)

for _ in range(2000):
    customer_id = random.randint(1, 2001)
    employee_id = random.randint(1, 2001)
    order_date = fake.date_time_between(start_date=start_date, end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    total_amount = round(random.uniform(10, 500), 2)

    query = """
    INSERT INTO orders (CustomerID, EmployeeID, OrderDate, TotalAmount) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (customer_id, employee_id, order_date, total_amount))

conn.commit()
cursor.close()
conn.close()
