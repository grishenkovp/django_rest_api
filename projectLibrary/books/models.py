from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=250, verbose_name='Подзаголовок')
    author = models.ForeignKey(User,on_delete=models.CASCADE,  verbose_name='Автор')
    isbn = models.CharField(max_length=13, blank=True, null=True, verbose_name='ISBN')

    class Meta:
        ordering = ('author',)
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
