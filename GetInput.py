from Meal import Meal
from ShoppingList import ShoppingList
from MealService import MealService
from Ingredient import Ingredient
isIngredient = False
userInput = True
myList = ShoppingList()

while (userInput == True):
    if (isIngredient == False):
        mealInput = Meal(input('Enter meal name: '))
        isIngredient = True
        x = input('Enter ingredient for your meal. ')
        mealInput.addIngredient(Ingredient(x))
    else:
        x = input('Enter another ingredient for your meal, or enter "+" to add a new meal. Enter "F" to finish. ')
        if (x != '+' and x != "F" and x != "f"):
            mealInput.addIngredient(Ingredient(x))
        elif (x == '+'):
            MealService.save(mealInput)
            myList.addIngredientsToList(mealInput.getMealList())
            mealInput.clearMeal()
            isIngredient = False
        else:
            userInput = False
            MealService.save(mealInput)
            myList.addIngredientsToList(mealInput.getMealList())
            for ingredient in myList.getIngredients():
                print (ingredient.name)
            
