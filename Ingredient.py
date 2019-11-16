import sqlite3

class Ingredient:

    def __init__(self, price = 0):
        self.id = None 
        self.price = price
    
    def getPrice(self):
        return self.price

    def save(self):
        if self.id is not None:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute("INSERT INTO ingredients VALUES (?, ?)", [self.name, self.price])
            self.id = c.lastrowid
            conn.commit()
            conn.close()
