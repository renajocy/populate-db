from faker import Faker
import mysql.connector

fake = Faker()

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cafeteria'
)
cursor = conn.cursor()

for _ in range(2000):
    name = fake.company()
    contact_number = fake.phone_number()
    address = fake.address()
    email = fake.company_email()

    query = """
    INSERT INTO suppliers (Name, ContactNumber, Address, Email) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, contact_number, address, email))

conn.commit()
cursor.close()
conn.close()
