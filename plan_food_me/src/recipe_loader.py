from plan_food_me.src.recipe import Recipe


class RecipeLoader:
    def __init__(self):
        self.breakfasts = []
        self.lunches = []
        self.dinners = []

    def create_meal_plan(self, file_name):

        with open(file_name, 'r') as f:

            should_read_recipe = True
            while should_read_recipe:
                line = f.readline()
                if line == '':
                    should_read_recipe = False
                else:
                    recipe = self.read_recipe(f, line)
                    self.add_recipe_to_menu(recipe)
            meals = {
                "breakfast": self.breakfasts,
                "lunch": self.lunches,
                "dinner": self.dinners
            }
            return meals


    def print_menu(self):
        for breakfast in self.breakfasts:
            print(breakfast)
        for lunch in self.lunches:
            print(lunch)
        for dinner in self.dinners:
            print(dinner)

    def read_recipe(self, f, line):
        recipe_ingredients = []

        recipe_type = line.rstrip()
        recipe_name = f.readline().rstrip()

        should_read_ingredients = True
        while should_read_ingredients:
            recipe_ingredient = f.readline().rstrip()
            if recipe_ingredient == '':
                should_read_ingredients = False
            else:
                recipe_ingredients.append(recipe_ingredient)

        recipe = Recipe(recipe_type, recipe_name, recipe_ingredients)
        return recipe

    def add_recipe_to_menu(self, recipe):
        if recipe.recipe_type == 'breakfast':
            self.breakfasts.append(recipe)
        elif recipe.recipe_type == 'lunch':
            self.lunches.append(recipe)
        elif recipe.recipe_type == 'dinner':
            self.dinners.append(recipe)