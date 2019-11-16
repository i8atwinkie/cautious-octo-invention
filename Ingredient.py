class Ingredient:

    def __init__(self, name = "", price = 0):
        self.__price = price
        self.__name = name
    
    def getPrice(self):
        return self.__price
