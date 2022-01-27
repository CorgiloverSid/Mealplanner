class RecipeGenerator:
    def __init__(self, recipe_book):
        self.recipe_book = recipe_book

    def generate_recipes(self, requested_amount):

        generated_recipes = []

        for meal_type in self.recipe_book:
            self.get_recipes(self.recipe_book[meal_type], generated_recipes, requested_amount)

        return generated_recipes

    def get_recipes(self, recipes, generated_recipes, amount):
        for index in range(int(amount)):
            if len(recipes) > index:
                generated_recipes.append(recipes[index])