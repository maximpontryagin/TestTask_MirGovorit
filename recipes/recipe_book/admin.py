from django.contrib import admin

from .models import Product, Recipe, RecipeProduct


admin.site.register(Product)
admin.site.register(Recipe)


@admin.register(RecipeProduct)
class IngredientInRecipe(admin.ModelAdmin):
    list_display = ('recipe', 'product', 'weight')