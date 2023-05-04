from django.shortcuts import render    # imported by default
# Displays list and details
from django.views.generic import ListView, DetailView
# This will access Recipe model
from .models import Recipe

# Create your views here.


def home(request):
    return render(request, 'recipes/recipes_home.html')


# Listview package is a class-based view used to display a list of objects

class RecipeListView(ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/main.html'  # specify template

# Detailview is a class-based view used to display data details


class RecipeDetailView(DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template
