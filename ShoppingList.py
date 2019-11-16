import Meal

class ShoppingList:
    def __init__(self, meals = []):
        self.meals = meals

    def getTotalPrice(self):
        total = 0
        for meal in meals:
            total += meal.getPrice
        return total
        

