from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    """Город к которому объявления относится"""
    # Могут быть города с одинаковымы назаваниями
    # можно сделать комбинированный ключ из 
    # страны, области и города
    name = models.Model(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Classfield(models.Model):
    """Объявление"""
    header = models.CharField()
    body = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Counter(models.Model):
    """Счетчик просмотра объявлений"""
    classfield = models.ForeignKey(Classfield, on_delete=models.CASCADE)
    value = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчики'
