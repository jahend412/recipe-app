from django.shortcuts import render    # imported by default
# Displays list and details
from django.views.generic import ListView, DetailView
# This will access Recipe model
from .models import Recipe
# to protect class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# to protect function-based views
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request, 'recipes/recipes_home.html')


# Listview package is a class-based view used to display a list of objects

class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/main.html'  # specify template

# Detailview is a class-based view used to display data details


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = 'recipes/detail.html'  # specify template

# Define function-based view - records(records()
# KEEP PROTECTED   -   @login_required


@login_required
def records(request):
    # do nothing, simply display page
    return render(request, 'recipes/records.html')
