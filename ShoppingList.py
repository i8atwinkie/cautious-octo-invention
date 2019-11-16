from Meal import Meal
from ShoppingListIngredient import ShoppingListIngredient

class ShoppingList:
    def __init__(self, ingredients = []):
        self.shoppingListIngredients = []
        for ingredient in ingredients:
            self.shoppingListIngredients.append(ShoppingListIngredient(ingredient))

    def getIngredients(self):
        ingredients = []
        for shoppingListIngredient in self.shoppingListIngredients:
            ingredients.append(shoppingListIngredient.ingredient)
        return ingredients

    def getTotalPrice(self):
        total = 0
        for shoppingListIngredient in self.shoppingListIngredients:
            total += shoppingListIngredient.getPrice
        return total

    def getCheckedOffPrice(self):
        total = 0
        for shoppingListIngredient in self.shoppingListIngredients:
            if shoppingListIngredient.checkedOff is True:
                total += shoppingListIngredient.getPrice
        return total

    def getCheckedOffIngredients(self):
        shoppingListIngredients = []
        for shoppingListIngredient in self.shoppingListIngredients:
            if shoppingListIngredient.checkedOff is True:
                shoppingListIngredients.append(shoppingListIngredient)
        return shoppingListIngredients

    # def checkOffIngredient(self, shoppingListIngredient):
    #     shoppingListIngredient.checkOffIngredient()

    def addIngredientToList(self, ingredient):
        unique = True
        for i in self.shoppingListIngredients:
            if (ingredient.name == i.ingredient.name):
                unique = False
        if (unique == True):
            self.shoppingListIngredients.append(ShoppingListIngredient(ingredient))

    def addIngredientsToList(self, ingredients):
        for ingredient in ingredients:
            self.addIngredientToList(ingredient)

    def addMealToList(self, meal):
        for ingredient in meal:
            self.shoppingListIngredients.append(ShoppingListIngredient(ingredient))