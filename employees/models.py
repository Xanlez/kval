from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Должность')
    hire_date = models.DateField(verbose_name='Дата приёма')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    email = models.EmailField(max_length=100, unique=True, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        db_table = 'employees'
        ordering = ['full_name']
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.full_name
