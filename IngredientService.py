import sqlite3

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
    def save(ingredient):
            if ingredient.id is None:
                conn = sqlite3.connect('database.db')
                c = conn.cursor()
                c.execute("INSERT INTO ingredients VALUES (?, ?, ?)", [None, ingredient.name, ingredient.price])
                ingredient.id = c.lastrowid
                conn.commit()
                conn.close()