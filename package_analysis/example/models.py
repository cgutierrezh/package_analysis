from django.db import models

class Tshirt(models.Model):
    name = models.CharField('Hi, im a name', max_length=10 ,blank=True)
    size = models.CharField(
        'Im the size', max_length=1, blank=True,
        choices=(('S', 'Small'), ('M', 'Medium'), ('L', 'Large')))

