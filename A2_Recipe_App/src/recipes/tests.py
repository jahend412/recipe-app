from django.test import TestCase
# Access the Recipe model
from .models import Recipe

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Tea', cooking_time=5, ingredients='tea-leaves, water, honey',
                              description='Add tea leaves to boiling water, then add honey')

    def test_desciption(self):
        recipe = Recipe.objects.get(id=1)
        name_max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(name_max_length, 120)

    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        recipe_name_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(recipe_name_label, 'name')

    def test_cookingtime_helptext(self):
        recipe = Recipe.objects.get(id=1)
        recipe_cookingtime = recipe._meta.get_field('cooking_time').help_text
        self.assertEqual(recipe_cookingtime, 'In minutes')

    def test_get_absolute_url(self):
        # get absolute_url takes you to the detail page of the first recipe
        recipe = Recipe.objects.get(id=1)
        # Loads to the url /recipes/list/1
        self.assertEqual(recipe.get_absolute_url(), '/recipes/list/1')

    def test_difficulty_calcuation(self):
        # Testing the calculate_difficulty function
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(recipe.calculate_difficulty(), 'Hard')
