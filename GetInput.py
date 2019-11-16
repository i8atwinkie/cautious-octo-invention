from Meal import Meal
from ShoppingList import ShoppingList
isIngredient = False
userInput = True

while (userInput == True):
    if (isIngredient == False):
        mealInput = Meal(input('Enter meal name: '))
        isIngredient = True
        x = input('Enter ingredient for your meal. ')
        mealInput.addIngredient(x)
    else:
        x = input('Enter another ingredient for your meal, or enter "+" to add a new meal. Enter "F" to finish. ')
        if (x != '+' and x != "F" and x != "f"):
            mealInput.addIngredient(x)
        elif (x == '+'):
            
            isIngredient = False
        else:
            userInput = False
            
