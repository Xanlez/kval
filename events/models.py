from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    location = models.CharField(max_length=150, verbose_name='Место проведения')
    event_date = models.DateTimeField(verbose_name='Дата и время')
    max_guests = models.IntegerField(verbose_name='Макс. гостей')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')

    class Meta:
        ordering = ['event_date']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title
