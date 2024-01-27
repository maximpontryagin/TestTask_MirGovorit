from django.urls import path

from . import views

app_name = 'brecipe_book'

urlpatterns = [
    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>',
         views.add_product_to_recipe),
    path('cook_recipe/<int:recipe_id>', views.cook_recipe),
    path('show_recipes_without_product/<int:product_id>',
         views.show_recipes_without_product),

]
