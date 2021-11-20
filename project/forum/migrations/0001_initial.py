# Generated by Django 3.2.9 on 2021-11-20 17:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('desc', models.CharField(max_length=512, verbose_name='Описание')),
                ('registered_in', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('registered_in', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Сообщение')),
                ('registered_in', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum', verbose_name='Форум')),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
        migrations.AddField(
            model_name='forum',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.group', verbose_name='Группа'),
        ),
    ]
