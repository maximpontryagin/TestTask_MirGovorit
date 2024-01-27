from django.db import models


class Product(models.Model):
    """Модель Продуктов."""

    title = models.CharField('Название продукта', max_length=256)
    number_prepared = models.IntegerField(
        'количество приготовленных блюд для каждого продукта', default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Recipe(models.Model):
    """Модель Рецепта."""

    title = models.CharField('Название рецепта', max_length=256)
    products = models.ManyToManyField(Product, verbose_name='Продукты',
                                      through='RecipeProduct')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class RecipeProduct(models.Model):
    """Модель связывающая рецепты и прокудты связью ManyToMany."""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    weight = models.IntegerField('Вес продукта в граммах', default=0)

    class Meta:
        verbose_name = 'Редактирование рецептов'
        verbose_name_plural = 'Редактирование рецептов'

    def __str__(self):
        return (
            f'{self.recipe.title} ({self.product.title}) - {self.weight} '
        )
