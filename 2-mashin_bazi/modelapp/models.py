from django.db import models

class Factory(models.Model):
    name = models.CharField(max_length=10)

class Car(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10, choices=[('w', 'white'), ('b', 'black')])
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    price = models.IntegerField()