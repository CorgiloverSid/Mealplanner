class Recipe:
    def __init__(self, recipe_type, recipe_name, recipe_ingredients):
        self.recipe_type = recipe_type
        self.recipe_name = recipe_name
        self.recipe_ingredients = recipe_ingredients

    def __str__(self):
        recipe_string = f"\n{self.recipe_type}\n{self.recipe_name}\n"
        for ingredient in self.recipe_ingredients:
            recipe_string += ingredient + ' '
        return recipe_string

    def get_ingredients(self):
        return self.recipe_ingredients

    def get_recipe_name(self):
        return self.recipe_name

