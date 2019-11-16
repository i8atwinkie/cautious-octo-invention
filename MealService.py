from Meal import Meal
from IngredientService import IngredientService
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

        return MealService.dataToObject(meals)

    @staticmethod
    def findNameLike(search):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM meals WHERE name LIKE ?", ("%" + search + "%",))
        meals = c.fetchall()
        conn.commit()
        conn.close()

        return MealService.dataToObject(meals)

    @staticmethod
    def save(meal):
            if meal.id is None:
                conn = sqlite3.connect('database.db')
                c = conn.cursor()
                c.execute("INSERT INTO meals VALUES (?, ?)", [None, meal.name])
                meal.id = c.lastrowid

                conn.commit()
                conn.close()
                
                for ingredient in meal.ingredients:
                    if ingredient.id is None:
                        IngredientService.save(ingredient)
                    conn = sqlite3.connect('database.db')
                    c = conn.cursor()
                    c.execute("INSERT INTO meal_ingredients VALUES (?, ?, ?)", [None, meal.id, ingredient.id])
                    conn.commit()
                    conn.close()

    @staticmethod
    def dataToObject(mealsData):
        mealObjs = []
        for mealData in mealsData:
            mealObjs.append(Meal(mealData[1], 
            IngredientService.findByMealId(mealData[0]),
            mealData[0]))

        return mealObjs
