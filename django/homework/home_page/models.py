from django.db import models
from datetime import date


class Lesson(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Название предмета')
    slug = models.SlugField(unique=True)
    

    def __str__(self):
        return self.name

class Homework(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Название Д/З')
    slug = models.SlugField(unique=True)
    file = models.FileField(upload_to='files/')
    description = models.TextField(verbose_name='Описание', null=True)
    publication_date = models.DateField(default=date.today, verbose_name='Дата публикации Д/З')
    expiration_date = models.DateField(verbose_name='Срок сдачи Д/З')
    homework = models.ForeignKey(Lesson, verbose_name='Предмет', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


