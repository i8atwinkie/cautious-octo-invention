class Ingredient:

    def __init__(self, name = "", price = None, id = None):
        self.price = price
        self.name = name
        self.id = id
    
    def getPrice(self):
        return self.price
