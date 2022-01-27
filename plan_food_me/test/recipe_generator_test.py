import unittest
from plan_food_me.src.recipe_generator import RecipeGenerator


class TestStringMethods(unittest.TestCase):

    def test_generate_requested_amount_when_enough_recipes(self):
        meal_plan = {
            "breakfast": ["pancake", "cereal"],
            "lunch": ["sandwich", "bagel"],
            "dinner": ["fried chicken", "steak"]
        }
        recipe_generator = RecipeGenerator(meal_plan)
        generated_recipes = recipe_generator.generate_recipes(2)

        expected_recipes = ["pancake", "cereal", "sandwich", "bagel", "fried chicken", "steak"]
        self.assertEqual(generated_recipes, expected_recipes)

    def test_generate_max_available_when_not_enough_recipes(self):
        meal_plan = {
            "breakfast": ["pancake", "cereal"],
            "lunch": ["sandwich", "bagel"],
            "dinner": ["pie"]
        }
        recipe_generator = RecipeGenerator(meal_plan)
        generated_recipes = recipe_generator.generate_recipes(2)

        expected_recipes = ["pancake", "cereal", "sandwich", "bagel", "pie"]
        self.assertEqual(expected_recipes, generated_recipes)




if __name__ == '__main__':
    unittest.main()