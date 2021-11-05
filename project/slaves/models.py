from django.contrib.auth.models import User
from django.db import models


class Resume(models.Model):
    """Описывает резюме раба"""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец')
    phone = models.CharField('Телефон', max_length=32, default='неизвествен')
    title = models.CharField('Название', max_length=128)
    money = models.PositiveIntegerField('Желаемая заплата')
    skill = models.TextField('Навыки', help_text='Напиши обо всём, что умеешь')
    education = models.CharField('Образование', max_length=1024, blank=True, null=True)
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.money}'


class Place(models.Model):
    """Описывает место работы раба"""
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, verbose_name='Резюме')
    title = models.CharField(verbose_name='работодатель', max_length=128)
    position = models.CharField(verbose_name='должность', max_length=128)
    duty = models.TextField('Обязанности', blank=True, null=True)
    started_in = models.DateField('Начал работать')
    finished_in = models.DateField('Закончил работать', blank=True, null=True)
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.position}'
