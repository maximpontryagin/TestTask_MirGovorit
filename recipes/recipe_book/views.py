from django.shortcuts import render

from .models import Product, Recipe, RecipeProduct


def add_product_to_recipe(request, recipe_id, product_id, weight):
    """Функция добавления или обновления пробуктов в рецепте."""
    template_name = 'recipe_book/index.html'
    try:
        RecipeProduct.objects.get(recipe_id=recipe_id, product_id=product_id)
        RecipeProduct.objects.filter(
            recipe_id=recipe_id, product_id=product_id).update(weight=weight)
    except:
        RecipeProduct.objects.create(
            recipe_id=recipe_id, product_id=product_id, weight=weight)

    return render(request, template_name)


def cook_recipe(request, recipe_id):
    """Функция подсчета количества использования продуктов во всех рецептах."""
    template_name = 'recipe_book/count.html'
    products_id = RecipeProduct.objects.values(
        'product_id').filter(recipe_id=recipe_id)
    for product_id in products_id:
        product = Product.objects.get(pk=product_id['product_id'])
        product.number_prepared += 1
        product.save()
    return render(request, template_name)


def show_recipes_without_product(request, product_id):
    """Функция поиска отсуствия или малого присутсвия продукта в рецепте."""
    template_name = 'recipe_book/ShowRecipesWithouProduct.html'
    recipes_id_have_product = RecipeProduct.objects.filter(
        product_id=product_id, weight__gte=10).values('recipe_id')
    recipes = Recipe.objects.exclude(pk__in=recipes_id_have_product)
    context = {
        'recipes': recipes
    }
    return render(request, template_name, context)
