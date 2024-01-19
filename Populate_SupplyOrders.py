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

supplier_id_range = range(1, 2002)
employee_id_range = range(1, 2002)
order_id_range = range(1, 2002)

start_date = datetime.today() - timedelta(days=365)

for _ in range(2000):
    supplier_id = random.choice(supplier_id_range)
    employee_id = random.choice(employee_id_range)
    order_id = random.choice(order_id_range)
    order_date = fake.date_time_between(start_date=start_date, end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    total_amount = random.randint(100, 3000)

    query = """
    INSERT INTO supplyorders (SupplierID, OrderDate, TotalAmount, EmployeeID, OrderID) 
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (supplier_id, order_date, total_amount, employee_id, order_id))

conn.commit()
cursor.close()
conn.close()
