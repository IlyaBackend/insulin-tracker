'''Создаём модель, создаём бд, создаём SQLite'''

from django.db import models
from django.utils import timezone



class InsulinInjection(models.Model):
    date = models.DateTimeField(default=timezone.now) # Дата и время укола
    injected = models.BooleanField(default=False) # Индикатор, был ли укол
    notes = models.TextField(blank=True, null=True) # Заметки, но делать их необязательно

    def __str__(self):
        ''' Магический метод, который поможет отображаться в виде
        человекочитаемой строки'''
        status = 'Вколот' if self.injected else 'Пропущен'
        return f'{status} инсулин в {self.date}'
