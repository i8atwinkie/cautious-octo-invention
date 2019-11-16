import sqlite3

from IngredientService import IngredientService

from Meal import Meal
from ShoppingList import ShoppingList

class ShoppingListService:
    @staticmethod
    def get():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("SELECT * FROM shopping_list")
        shoppingListItemsData = c.fetchall()
        conn.commit()
        conn.close()

        shoppingListObj = ShoppingList()

        for shoppingListItemData in shoppingListItemsData:
            shoppingListObj.addIngredientToList(IngredientService.findById(shoppingListItemData[0]))

        return shoppingListObj

    @staticmethod
    def save(shoppingList):
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        for shoppingListItem in shoppingList.shoppingListIngredients:
            c.execute("INSERT INTO shopping_list VALUES (?, ?)", [shoppingListItem.ingredient.id, shoppingListItem.amount])
        conn.commit()
        conn.close()

    @staticmethod
    def delete():
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('DROP TABLE IF EXISTS shopping_list')
        c.execute('''CREATE TABLE shopping_list
             (ingredient_id integer, amount integer)''')
        conn.commit()
        conn.close()