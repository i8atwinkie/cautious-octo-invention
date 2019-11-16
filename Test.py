from MealService import MealService
from IngredientService import IngredientService
from ShoppingListService import ShoppingListService

from Meal import Meal
from Ingredient import Ingredient
from ShoppingList import ShoppingList


shoppingList = ShoppingList()


# MealService.save(Meal('Potato', [
#     Ingredient('Ground'),
#     Ingredient('Water')
# ]))

# MealService.save(Meal('Pickle', [
#     Ingredient('Vinegar'),
#     Ingredient('Cucumber')
# ]))

meals = MealService.all()
for meal in meals:
    print(meal.name)
    shoppingList.addMealToList(meal)
    for ingredient in meal.ingredients:
        print('\t' + ingredient.name)
        print('\t\t$' + str(ingredient.price))

print("=======================================")

meals = MealService.findNameLike('Pot')
for meal in meals:
    print(meal.name)
    for ingredient in meal.ingredients:
        print('\t' + ingredient.name)

print("=======================================")

ShoppingListService.save(shoppingList)
shoppingList = ShoppingListService.get()

for item in shoppingList.shoppingListIngredients:
    print(item.ingredient.name)
    print('\t$' + str(item.ingredient.price))
print('Total: $' + str(shoppingList.getTotalPrice()))


