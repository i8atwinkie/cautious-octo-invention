import Ingredient

class Meal: 

    def __init__(self):
        self.__ingredients = []
    
    def getMealList(self):
        return self.__ingredients
        
    def addIngredient(self, ingredient):
        self.__ingredients.append(ingredient)

    def getPrice(self):
        price = 0
        for i in self.__ingredients:
            price +=i.getPrice
        return price


