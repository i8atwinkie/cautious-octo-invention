class ShoppingListIngredient:
    def __init__(self, ingredient, amount = 1):
        self.ingredient = ingredient
        self.checkedOff = False
        self.amount = amount