from book import Book
from recipe import Recipe

r = Recipe("Pie", 1, 60, ["eggs", "dough", "salt", "pepper", "tomatoes"],
           "Mix all the ingredients and make your pie, you know how to do it mate", "lunch")
to_print = str(r)
print(to_print)
