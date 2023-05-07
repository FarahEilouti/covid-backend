from django.db import models

# Create your models here.
class Record(models.Model):
    country = models.CharField(max_length=255)
    date = models.DateField()

class AllCountries(models.Model):
    name = models.CharField(max_length=100)
    population = models.PositiveIntegerField()


    def __str__(self):
        return self.name    