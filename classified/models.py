from django.db import models
from django.contrib.auth.models import User

NEW = 0
PROCESSING = 1

STATES = ((NEW, 'New'), (PROCESSING, 'Proccessing'))

class City(models.Model):
    """Город к которому объявления относится"""

    # Могут быть города с одинаковыми названиями
    # можно сделать комбинированный ключ из 
    # страны, области и города
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Classified(models.Model):
    """Объявление"""
    header = models.CharField(max_length=255)
    body = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.PositiveIntegerField() # Количество просмотров объявления

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class ViewCounter(models.Model):
    """Счетчик просмотра объявлений.
    При просмотре объявления добавляется запись
    которая в последующем будет обработан Celery
    """
    classified = models.ForeignKey(Classified, on_delete=models.CASCADE)
    state = models.PositiveIntegerField(choices=STATES)

    def __str__(self):
        return "{} - {}".format(self.classified, self.state)

    class Meta:
        verbose_name = 'Счетчик'
        verbose_name_plural = 'Счетчики'
