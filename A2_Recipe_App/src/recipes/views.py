from django.shortcuts import render    # imported by default
# Displays list and details
from django.views.generic import ListView, DetailView
# This will access Recipe model
from .models import Recipe
# to protect class-based views
from django.contrib.auth.mixins import LoginRequiredMixin
# to protect function-based views
from django.contrib.auth.decorators import login_required

from .forms import RecipeSearchForm
import pandas as pd
from .utils import get_chart

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

    # create an instance of RecipeSearchForm that you defined in recipes/forms.py
    form = RecipeSearchForm(request.POST or None)
    recipe_df = None  # initialize dataframe to None
    recipe_diff = None
    chart = None  # initialize chart to None
    qs = None

    # check if the button is clicked
    if request.method == 'POST':
        recipe_diff = request.POST.get('recipe_diff')  # read recipe_name
        chart_type = request.POST.get('chart_type')  # read recipe chart type

        if recipe_diff == '#1':
            recipe_diff = 'Easy'
        if recipe_diff == '#2':
            recipe_diff = 'Medium'
        if recipe_diff == '#3':
            recipe_diff = 'Intermediate'
        if recipe_diff == '#4':
            recipe_diff = 'Hard'

        # apply filter to extract data
        qs = Recipe.objects.all()
        id_searched = []
        for obj in qs:
            diff = obj.calculate_difficulty()
            if diff == recipe_diff:
                id_searched.append(obj.id)

        qs = qs.filter(id__in=id_searched)

        if qs:  # if the data is found, convert the queryset values to pandas dataframe
            recipe_df = pd.DataFrame(qs.values())
            chart = get_chart(chart_type, recipe_df,
                              labels=recipe_df['name'].values)

            # convert the dataframe to HTML
            recipe_df = recipe_df.to_html()

    # print(recipe_diff)
    # pack up data to be sent to template in the context dictionary
    context = {
        'form': form,
        'recipe_df': recipe_df,
        'recipe_diff': recipe_diff,
        'chart': chart,
        'qs': qs,
    }

    # load the template and send the context dictionary to template
    return render(request, 'recipes/records.html', context)
