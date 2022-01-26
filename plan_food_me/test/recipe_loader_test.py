import unittest
from plan_food_me.src.recipe_loader import RecipeLoader


class TestStringMethods(unittest.TestCase):

    def test_recipes_are_loaded_for_valid_file(self):
        recipe_loader = RecipeLoader()
        meal_plan = recipe_loader.create_meal_plan("test_recipes")

        breakfasts = meal_plan["breakfast"]
        expected_ingredients = ["egg"]
        self.assertEqual(len(breakfasts), 2)
        self.assertEqual(breakfasts[0].get_recipe_name(), "pancake")
        self.assertEqual(breakfasts[0].get_ingredients(), expected_ingredients)
        self.assertEqual(len(meal_plan["lunch"]), 1)
        self.assertEqual(len(meal_plan["dinner"]), 2)


if __name__ == '__main__':
    unittest.main()