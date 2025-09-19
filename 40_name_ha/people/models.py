from django.db import models


class Person(models.Model):
    # fullname = models.CharField(max_length=250, null=True)
    # information = models.CharField(max_length=350, null=True)
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    id_code = models.CharField(max_length=10)
    born_in = models.CharField(max_length=30)
    birth_year = models.PositiveIntegerField()