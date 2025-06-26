from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва категорії')
    description = models.TextField(blank=True, verbose_name='Опис категорії')

    def __str__(self):
        return self.name

class Product(models.Model):
    # Мінімум 8 філдів, з дефолтами та field options
    name = models.CharField(max_length=200, verbose_name='Назва товару')
    description = models.TextField(blank=True, verbose_name='Опис')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Ціна')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Кількість на складі')
    available = models.BooleanField(default=True, verbose_name='В наявності')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категорія')
    sku = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.name