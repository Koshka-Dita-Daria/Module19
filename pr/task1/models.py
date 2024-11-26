from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=1000000, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=9, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=4)
    description = models.CharField(max_length=10000000)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(to=Buyer, related_name='games')

    def __str__(self):
        return self.title