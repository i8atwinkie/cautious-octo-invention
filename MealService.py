from Meal import Meal
from Ingredient import Ingredient
import sqlite3

class MealService:
    @staticmethod
    def all():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM meals")
        meals = c.fetchall()
        conn.commit()
        conn.close()

        for meal in meals:
            print(meal)

        return meals


    @staticmethod
    def save(meal):
            if meal.id is not None:
                conn = sqlite3.connect('database.db')
                c = conn.cursor()
                c.execute("INSERT INTO meals VALUES (?, ?)", [None, meal.name])
                meal.id = c.lastrowid
                
                for ingredient in meal.ingredients:
                    if ingredient.id is None:
                        ingredient.save()
                    c.execute("INSERT INTO meal_ingredients VALUES (?, ?)", [meal.id, ingredient.id])

                conn.commit()
                conn.close()