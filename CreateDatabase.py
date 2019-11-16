import sqlite3

conn = sqlite3.connect('database.db')

c = conn.cursor()

# Create table
c.execute('DROP TABLE IF EXISTS ingredients')
c.execute('''CREATE TABLE ingredients
             (id integer PRIMARY KEY, name text, price real)''')

c.execute('DROP TABLE IF EXISTS meals')
c.execute('''CREATE TABLE meals
             (id integer PRIMARY KEY, name text)''')

c.execute('DROP TABLE IF EXISTS meal_ingredients')
c.execute('''CREATE TABLE meal_ingredients
             (id integer PRIMARY KEY, meal_id integer, ingredient_id integer)''')

c.execute('DROP TABLE IF EXISTS shopping_list')
c.execute('''CREATE TABLE shopping_list
             (ingredient_id integer)''')

# Insert a row of data
# c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
