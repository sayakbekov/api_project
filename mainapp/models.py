from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Nout(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    model = models.CharField(max_length=255, verbose_name='Модель')
    pam = models.CharField(max_length=255, verbose_name='Память')
    po = models.CharField(max_length=255, verbose_name='Оперативка')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'
