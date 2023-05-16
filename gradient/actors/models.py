from django.db import models


class ActorImage(models.Model):
    images = models.ImageField(
        upload_to='photos',
        verbose_name='Фото'
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=40
    )

    class Meta:
        verbose_name = 'Фото актёров'
        verbose_name_plural = 'Фото актёров'

    def __str__(self):
        return f"{self.last_name}"


class Actor(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=30
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=40
    )
    age = models.IntegerField(verbose_name='Возраст')
    town = models.CharField(max_length=30, verbose_name='Город')
    height = models.IntegerField(verbose_name='Рост')
    body = models.CharField(max_length=30, verbose_name='Телосложение')
    hair_col = models.CharField(max_length=30, verbose_name='Цвет волос')
    eyes_col = models.CharField(max_length=30, verbose_name='Цвет глаз')
    person = models.CharField(max_length=30, verbose_name='Внешность')
    education = models.CharField(max_length=30, verbose_name='Образование')
    language = models.CharField(max_length=30, verbose_name='Языки')
    roles = models.TextField(verbose_name='Роли в кино')
    skills = models.TextField(verbose_name='Навыки')
    images = models.ManyToManyField(ActorImage, related_name='Фото')
    enable = models.BooleanField(verbose_name='Активен?')

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'

    def __str__(self):
        return f"{self.name} {self.last_name}"
