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
    name = fake.name()
    contact = fake.phone_number()
    email = fake.email()
    loyalty_points = fake.random_int(min=0, max=100)

    query = "INSERT INTO customers (Name, ContactNumber, Email, LoyaltyPoints) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, contact, email, loyalty_points))

conn.commit()
cursor.close()
conn.close()
