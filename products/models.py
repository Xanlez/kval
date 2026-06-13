from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    category = models.CharField(max_length=100, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    sku = models.CharField(max_length=50, unique=True, verbose_name='Артикул')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name
