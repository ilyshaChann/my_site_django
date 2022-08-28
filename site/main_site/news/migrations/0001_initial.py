# Generated by Django 4.0.6 on 2022-08-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=150, verbose_name='Анонс')),
                ('photos', models.ImageField(upload_to='img')),
                ('text', models.TextField(verbose_name='Основной текст')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),
                ('photo', models.ImageField(upload_to='img')),
            ],
        ),
    ]
