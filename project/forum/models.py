from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Group(models.Model):
    """Группа форумов"""

    title = models.CharField('Заголовок', max_length=128)
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return self.title


class Forum(models.Model):
    """Форум"""

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name='Группа')
    title = models.CharField('Заголовок', max_length=128)
    desc = models.CharField('Описание', max_length=512)
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/forum/{self.pk}/'


class Post(models.Model):
    """Запись в форуме"""
    forum = models.ForeignKey(
        Forum, on_delete=models.CASCADE, verbose_name='Форум')
    text = models.TextField('Сообщение')
    registered_by = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name='Автор')
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        if len(self.text) > 100:
            return f'{self.text[:100]}...'
        return self.text

    def get_absolute_url(self):
        return f'/forum/post/{self.pk}/'


class Reply(models.Model):
    """Отклики на запись"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Отклик')
    text = models.TextField('Сообщение')
    registered_by = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name='Автор')
    registered_in = models.DateTimeField('Создано', auto_now_add=True)

    def __str__(self):
        if len(self.text) > 100:
            return f'{self.text[:100]}...'
        return self.text

    def get_absolute_url(self):
        return f'/forum/post/{self.post.pk}/' ##reply_{self.pk}'
