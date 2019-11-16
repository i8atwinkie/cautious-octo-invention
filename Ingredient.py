class Ingredient:

    def __init__(self, name = "", price = 0, id = None):
        self.price = price
        self.name = name
        self.id = id
    
    def getPrice(self):
        return self.price
