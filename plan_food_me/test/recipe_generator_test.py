import unittest
from plan_food_me.src.recipe_generator import RecipeGenerator
from unittest.mock import patch


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

    def test_generate_recipes_not_picked_previously(self):
        meal_plan = {
            "breakfast": ["pancake", "cereal", "sausage", "baked beans"],
            "lunch": ["sandwich", "bagel", "burger", "hot dog"],
            "dinner": ["pie", "pizza", "risotto", "fish tacos"]
        }
        recipe_generator = RecipeGenerator(meal_plan)
        generated_recipes = recipe_generator.generate_recipes(1)

        expected_recipes = ["pancake", "sandwich", "pie"]
        self.assertEqual(expected_recipes, generated_recipes)

        generated_recipes = recipe_generator.generate_recipes(2)
        expected_recipes = ["cereal", "sausage", "bagel", "burger", "pizza", "risotto"]
        self.assertEqual(expected_recipes, generated_recipes)











if __name__ == '__main__':
    unittest.main()