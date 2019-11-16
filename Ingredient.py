class Ingredient:

    def __init__(self, name = "", price = 0):
        self.price = price
        self.name = name
        self.id = None
    
    def getPrice(self):
        return self.price
