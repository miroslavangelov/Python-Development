from django.urls import path

from recipes_app.views import index, create_recipe, edit_recipe, recipe_details, delete_recipe

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_recipe, name='create_recipe'),
    path('edit/<int:recipe_id>', edit_recipe, name='edit_recipe'),
    path('details/<int:recipe_id>', recipe_details, name='recipe_details'),
    path('delete/<int:recipe_id>', delete_recipe, name='delete_recipe'),
]
