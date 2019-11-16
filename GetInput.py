from Meal import Meal
from ShoppingList import ShoppingList
from MealService import MealService
from Ingredient import Ingredient
isIngredient = False
userInput = True
myList = ShoppingList()
total = 0

while (userInput == True):
    if (isIngredient == False):
        mealInput = Meal(input('Enter meal name: '))
        isIngredient = True
        ingred = input('Enter ingredient for your meal. ')
        pri = float(input('Enter ingredient price. (If price is unkown, input "0") $'))
        mealInput.addIngredient(Ingredient(ingred, pri))
    else:
        ingred = input('Enter another ingredient for your meal, or enter "+" to add a new meal. Enter "F" to finish. ')
        if (ingred != '+' and ingred != "F" and ingred != "f"):
            pri = float(input('Enter ingredient price. (If price is unkown, input "0") $'))
            mealInput.addIngredient(Ingredient(ingred, pri))
        elif (ingred == '+'):
            MealService.save(mealInput)
            myList.addIngredientsToList(mealInput.getMealList())
            mealInput.clearMeal()
            isIngredient = False
        else:
            userInput = False
            MealService.save(mealInput)
            myList.addIngredientsToList(mealInput.getMealList())
            print ("\n")
            for ingredient in myList.getIngredients():
                print ( str(ingredient.name) + ' $' + f'{ingredient.price:.2f}')
                total = total + ingredient.price
            print ('Total $' + f'{total:.2f}')
            
