import Ingredient
import sqlite3

class Meal: 

    def __init__(self, name = '', ingredients = []):
        self.name = name
        self.__ingredients = ingredients
    
    def getMealList(self):
        return self.__ingredients
        
    def addIngredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def getPrice(self):
        price = 0
        for i in self.__ingredients:
            price +=i.getPrice()
        return price

    def save(self):        
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO meals VALUES (?)", [self.name])
        conn.commit()
        conn.close()

