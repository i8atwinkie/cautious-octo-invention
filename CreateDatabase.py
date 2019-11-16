import sqlite3

from MealService import MealService

from Meal import Meal
from Ingredient import Ingredient

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
             (ingredient_id integer, amount integer)''')

# SEED
MealService.save(Meal('Potato', [
    Ingredient('Ground', 50),
    Ingredient('Water', 1)
]))

MealService.save(Meal('Pickle', [
    Ingredient('Vinegar', 19.5),
    Ingredient('Cucumber', 0.05)
]))

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
