from django.db import models

# Create your models here.
class Record(models.Model):
    country = models.CharField(max_length=255)
    date = models.DateField()

class AllCountries(models.Model):
    country_name = models.CharField(max_length=255)
    population = models.IntegerField()    