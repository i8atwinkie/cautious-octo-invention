import Meal
import ShoppingListIngredient

class ShoppingList:
    def __init__(self, ingredients = []):
        self.shoppingListIngredients = []
        for shoppingListIngredient in shoppingListIngredients:
            self.shoppingListIngredients.append(ShoppingListIngredient(ingredient))

    def getTotalPrice(self):
        total = 0
        for shoppingListIngredient in shoppingListIngredients:
            total += ingredient.getPrice
        return total

    def getCheckedOffPrice(self):
        total = 0
        for shoppingListIngredient in shoppingListIngredients:
            if shoppingListIngredient.checkedOff is true:
                total += ingredient.getPrice
        return total

    def getCheckedOffIngredients(self):
        shoppingListIngredients = []
        for shoppingListIngredient in self.shoppingListIngredients:
            if shoppingListIngredient.checkedOff is true:
                shoppingListIngredients.append(shoppingListIngredient)
        return shoppingListIngredients

    # def checkOffIngredient(self, shoppingListIngredient):
    #     shoppingListIngredient.checkOffIngredient()

    def addIngredientToList(self, ingredient):
        self.shoppingListIngredients.append(ShoppingListIngredient(ingredient))

    def addIngredientsToList(self, ingredients):
        for ingredient in ingredients:
            self.addIngredientToList(ingredient)

    def addMealToList(self, meal):
        for ingredient in meal:
            self.shoppingListIngredients.append(ShoppingListIngredient(ingredient))