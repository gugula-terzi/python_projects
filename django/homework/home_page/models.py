from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from datetime import date


class Lesson(models.Model):
    
    name = models.CharField(max_length=255, verbose_name='Название предмета')
    slug = models.SlugField(unique=True)
    

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Homework(models.Model):
    
    title = models.CharField(max_length=255, verbose_name='Название Д/З')
    slug = models.SlugField(unique=True)
    file = models.FileField(upload_to='files/')
    description = models.TextField(verbose_name='Описание', null=True)
    author = models.ForeignKey(User, verbose_name='Автор публикации', on_delete=models.CASCADE)
    publication_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата публикации Д/З')
    expiration_date = models.DateTimeField(blank=True, null=True, verbose_name='Срок сдачи Д/З')
    lesson = models.ForeignKey(Lesson, verbose_name='Предмет', on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    def publish(self):
        self.expiration_date = timezone.now()

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('post-detail', kwargs=kwargs)
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'


