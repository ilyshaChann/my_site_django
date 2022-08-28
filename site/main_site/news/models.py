from django.db import models

class Article(models.Model):
    title = models.CharField('Название',max_length=100)
    anons = models.CharField('Анонс', max_length=150)
    text = models.TextField('Основной текст')
    date = models.DateTimeField('Дата публикации')
    photo = models.ImageField(upload_to='img')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'