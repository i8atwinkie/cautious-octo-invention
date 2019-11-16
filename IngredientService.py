import sqlite3

from Ingredient import Ingredient

class IngredientService:

    @staticmethod
    def all():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ingredients")
        ingredients = c.fetchall()
        conn.commit()
        conn.close()

        for ingredient in ingredients:
            print(ingredient)

        return ingredients

    @staticmethod
    def findByMealId(mealId):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM ingredients INNER JOIN meal_ingredients ON ingredients.id = meal_ingredients.ingredient_id WHERE meal_id = ?", (mealId,))
        ingredients = c.fetchall()
        conn.commit()
        conn.close()

        ingredientObjs = []
        for ingredient in ingredients:
            ingredientObjs.append(Ingredient(ingredient[1], ingredient[2], ingredient[0]))

        return  ingredientObjs

    @staticmethod
    def save(ingredient):
            if ingredient.id is None:
                conn = sqlite3.connect('database.db')
                c = conn.cursor()
                c.execute("INSERT INTO ingredients VALUES (?, ?, ?)", [None, ingredient.name, ingredient.price])
                ingredient.id = c.lastrowid
                conn.commit()
                conn.close()