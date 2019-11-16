from Meal import Meal
from ShoppingList import ShoppingList
from MealService import MealService
from Ingredient import Ingredient
from ShoppingListService import ShoppingListService

isIngredient = False
userInput = True
myList = ShoppingList()
total = 0
canQuit = False

loadList = input('Would you like to load your last shopping list? (y,n)')
if (loadList == 'y' or loadList == 'Y'):
    myList = ShoppingListService.get()
    print('Shopping List:')
    for ingredient in myList.getIngredients():
        print ( str(ingredient.name) + ' $' + f'{ingredient.price:.2f}')
    print ('Total $' + str(myList.getTotalPrice()))
    print('You can now add more to your shopping list.')

while (userInput == True):
    if (isIngredient == False):
        count = 0
        choice = '0'
        if (canQuit == False):
            mealInput = Meal(input('Enter meal name: '))
        elif (canQuit == True):
            mealInput = Meal(input('Enter meal name, or enter "F" to finish. '))
        if (mealInput.name != "F" and mealInput.name != 'f'):
            results = MealService.findNameLike(mealInput.name)
            for result in results:
                count += 1
                print (str(count) + '. ' + result.name)
                resultIngredients = result.getMealList()
                for resultI in resultIngredients:
                    print (resultI.name)
            if (count > 0):
                choice = input('We found ' + str(count) + ' possible match(es) for your meal. Enter the number next to a meal to select it or enter "N" to create a new meal. ')
            if (count == 0 or choice == 'N' or choice == 'n'):   
                isIngredient = True
                ingred = input('Enter ingredient for your meal. ')
                pri = float(input('Enter ingredient price. (If price is unkown, input "0") $'))
                mealInput.addIngredient(Ingredient(ingred, pri))
            else:
                MealService.save(results[count-1])
                myList.addIngredientsToList(results[count-1].getMealList())
                mealInput.clearMeal()
                isIngredient = False
                canQuit = True
        else:
            userInput = False
            MealService.save(mealInput)
            myList.addIngredientsToList(mealInput.getMealList())
            print ("\n")
            for ingredient in myList.getIngredients():
                print ( str(ingredient.name) + ' $' + f'{ingredient.price:.2f}')
                total = total + ingredient.price
            print ('Total $' + f'{total:.2f}')

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

            
            
ShoppingListService.delete()
ShoppingListService.save(myList)

print('Saved shopping list.')