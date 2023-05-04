from django.db import models
from django.shortcuts import reverse

# Create your models here.


class Recipe (models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='In minutes')
    ingredients = models.CharField(max_length=400)
    description = models.TextField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def get_absolute_url(self):
        return reverse('recipes:detail', kwargs={'pk': self.pk})

    # calculate difficulty of recipe using cooking time and number of ingredients
    def calculate_difficulty(self):
        ingredients = self.ingredients.split(', ')
        if self.cooking_time < 10 and len(ingredients) < 4:
            difficulty = 'Easy'
        elif self.cooking_time < 10 and len(ingredients) >= 4:
            difficulty = 'Medium'
        elif self.cooking_time >= 10 and len(ingredients) < 4:
            difficulty = 'Intermediate'
        elif self.cooking_time >= 10 and len(ingredients) >= 4:
            difficulty = 'Hard'
        return difficulty

    def __str__(self):
        return str(self.name)
