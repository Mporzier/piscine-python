class Recipe:
    def __init__(
        self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type
    ):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.recipe_type = recipe_type
        self.ingredients = ingredients
        self.description = description

    def __str__(self):
        to_print = 'Recipe name: ' + self.name + '.\n'
        to_print += 'Cooking level: ' + str(self.cooking_lvl) + '.\n'
        to_print += 'Cooking time: ' + str(self.cooking_time) + '.\n'
        to_print += 'This recipe is a ' + self.recipe_type + '.\n'
        to_print += 'Ingredients: ' + ', '.join(self.ingredients) + '.\n'
        to_print += 'Description: ' + self.description + '.'
        return to_print
