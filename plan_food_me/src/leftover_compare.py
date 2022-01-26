class LeftoverComparer:
    def __init__(self, meal_plan):
        self.meal_plan = meal_plan

    def compare_leftovers(self, stored_leftovers, meal_type):

        recipes = self.meal_plan[meal_type]
        best_amount_of_intersection = 0
        best_recipe = None

        for recipe in recipes:

            ingredients_as_set = set(recipe.get_ingredients())
            intersection = ingredients_as_set.intersection(stored_leftovers)
            intersection_length = len(intersection)
            if intersection_length > best_amount_of_intersection:
                best_amount_of_intersection = intersection_length
                best_recipe = recipe

        return best_recipe
