import sys


cookbook = {
    'sandwich': {'ingredients': {'ham', 'bread', 'cheese', 'tomatoes'}, 'meal': 'lunch', 'prep_time': '10'},
    'cake': {'ingredients': {'flour', 'sugar', 'eggs'}, 'meal': 'dessert', 'prep_time': '60'},
    'salad': {'ingredients': {'avocado', 'arugula', 'tomatoes', 'spinach'}, 'meal': 'lunch', 'prep_time': '15'}
}


def printRecipe(recipe):
    line = cookbook.get(recipe)
    print("Recipe for", recipe + ':')
    print("Ingredients list:", line['ingredients'])
    print("To be eaten for", line['meal'] + '.')
    print("Takes", line['prep_time'], "minutes of cooking.")


def deleteRecipe(recipe):
    del cookbook[recipe]
    print("Recipe \"" + recipe + "\" deleted.")


def addRecipe():
    print("Please enter the recipe's name:")
    print(">> ", end='')
    name = input()
    print("Please enter the recipe's ingredients, separated by a space:")
    print(">> ", end='')
    ingredients = input()
    print("Please enter the meal corresponding to the recipe:")
    print(">> ", end='')
    meal = input()
    print("Please enter the preparation time of the recipe:")
    print(">> ", end='')
    prep_time = input()
    ingredients = tuple(ingredients.split(" "))
    line = {name: {'ingredients': {ingredients},
                   'meal': meal, 'prep_time': prep_time}}
    cookbook.update(line)
    print("Recipe added to the cookbook.")


def printCookbook():
    print("The cookbook contains the following recipes:")
    for name in cookbook:
        print(name)


while 1:
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    entry = ''
    isvalid = 0
    while isvalid == 0:
        print(">> ", end='')
        entry = input()
        if entry.isdigit():
            if (int(entry) >= 0) and (int(entry) <= 5):
                isvalid = 1
        if isvalid == 1:
            break
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
    choice = int(entry)
    if choice == 1:
        addRecipe()
    if choice == 2:
        print("Please enter the recipe's name to delete it:")
        print(">> ", end='')
        rec = input()
        if not rec in cookbook:
            print("Recipe not found. Please enter an existing recipe.")
        else:
            deleteRecipe(rec)
    if choice == 3:
        print("Please enter the recipe's name to get its details:")
        print(">> ", end='')
        rec = input()
        if not rec in cookbook:
            print("Recipe not found. Please enter an existing recipe.")
        else:
            printRecipe(rec)
    if choice == 4:
        printCookbook()
    if choice == 5:
        sys.exit()
