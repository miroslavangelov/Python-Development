from django.shortcuts import render, redirect

from recipes_app.forms import RecipeForm
from recipes_app.models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'index.html', context)


def create_recipe(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('recipes_app:index')

    return render(request, 'create.html', {'form': form})


def edit_recipe(request, recipe_id):
    current_recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(request.POST or None, instance=current_recipe)
    if form.is_valid():
        form.save()
        return redirect('recipes_app:index')

    return render(request, 'edit.html', {'form': form, 'recipe': current_recipe})


def delete_recipe(request, recipe_id):
    current_recipe = Recipe.objects.get(id=recipe_id)
    form = RecipeForm(request.POST or None, instance=current_recipe)
    if request.method == 'POST':
        current_recipe.delete()
        return redirect('recipes_app:index')

    return render(request, 'delete.html', {'form': form, 'recipe': current_recipe})


def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    ingredients = recipe.ingredients.split(",")
    return render(request, 'details.html', {'recipe': recipe, 'ingredients': ingredients})
