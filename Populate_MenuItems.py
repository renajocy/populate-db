from faker import Faker
import mysql.connector
import random

fake = Faker()

categories = [
    'Beverages', 'Breakfast', 'Sandwiches', 'Salads',
    'Soups', 'Desserts', 'Hot Meals', 'Snacks',
    'Sides', 'Vegetarian', 'Grilled'
]

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='cafeteria'
)
cursor = conn.cursor()

for _ in range(2000):
    name = fake.word().capitalize() + " " + fake.word().capitalize()
    description = fake.text(max_nb_chars=200)
    price = round(fake.random_number(digits=2) + fake.random_digit()/100, 2)
    category = random.choice(categories)

    query = """
    INSERT INTO menuitems (Name, Description, Price, Category) 
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, description, price, category))

conn.commit()
cursor.close()
conn.close()
