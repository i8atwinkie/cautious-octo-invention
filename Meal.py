import Ingredient
import sqlite3

class Meal: 
    def __init__(self, name = '', ingredients = []):
        self.id = None, 
        self.name = name
        self.ingredients = ingredients
    
    def getMealList(self):
        return self.ingredients
        
    def addIngredient(self, ingredient):
        self.ingredients.append(ingredient)

    def getPrice(self):
        price = 0
        for i in self.ingredients:
            price +=i.getPrice()
        return price

    def clearMeal(self):
        del self.ingredients [:]
        self.name = ''
        self.id

