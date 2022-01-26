from collections import Counter
from recipe import Recipe

class AddRecipeMenu:
    def __init__(self):
        return

    def ask_recipe_file(self):
        ask_file = input(f"Welcome to the FastFood app!\nPlease enter your file name: \n")
        return ask_file

    def enter_leftovers(self):
        left_over_ingredients = input("Enter your leftover ingredients separated by commas: ")
        stored_leftovers = left_over_ingredients.split(', ')
        # print(stored_leftovers)
        # for leftover in stored_leftovers:
        #     print(leftover)
        return stored_leftovers


    def choose_meal_type(self):
        # breakfasts = self.breakfasts
        meal_type = input("Enter the meal type for these chosen ingredients: ")
        return meal_type
        # if meal_type == "breakfast":
        #     for i in breakfasts:
        #         print(i)



if __name__ == '__main__':
    egg = 1










