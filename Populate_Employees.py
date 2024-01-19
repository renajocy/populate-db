from faker import Faker
import mysql.connector
from datetime import timedelta, datetime

fake = Faker()

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cafeteria'
)
cursor = conn.cursor()

start_date = datetime.today() - timedelta(days=20*365)

for _ in range(2000):
    name = fake.name()
    position = fake.job()
    hire_date = fake.date_between(start_date=start_date, end_date='today')
    contact_number = fake.phone_number()

    query = """
    INSERT INTO employees (Name, Position, HireDate, ContactNumber) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, position, hire_date, contact_number))

conn.commit()
cursor.close()
conn.close()
