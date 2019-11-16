class ingredient:

    def __init__(self):
        self.__price
    
    def getPrice(self):
        return self.__price

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


