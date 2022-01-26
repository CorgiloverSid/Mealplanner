import unittest
from plan_food_me.src.leftover_compare import LeftoverComparer
from plan_food_me.src.recipe import Recipe


class TestStringMethods(unittest.TestCase):

    def test_recipes_are_loaded_for_valid_file(self):
        recipe = Recipe("breakfast", "pancake", ["egg"])

        meal_plan = {
            "breakfast": [recipe],
            "lunch": [],
            "dinner": []
        }
        leftover_comparer = LeftoverComparer(meal_plan)
        leftover_recipe = leftover_comparer.compare_leftovers(["egg"], "breakfast")

        self.assertEqual(leftover_recipe.get_recipe_name(), "pancake")

    def test_recipe_with_most_leftover_ingredients_is_returned(self):
        meal_plan = {
            "breakfast": [Recipe("breakfast", "pancake", ["egg"]),
                          Recipe("breakfast", "omelette",  ["egg", "milk"])],
            "lunch": [],
            "dinner": []
        }

        leftover_comparer = LeftoverComparer(meal_plan)
        leftover_recipe = leftover_comparer.compare_leftovers(["egg", "milk"], "breakfast")

        self.assertEqual(leftover_recipe.get_recipe_name(), "omelette")



if __name__ == '__main__':
    unittest.main()