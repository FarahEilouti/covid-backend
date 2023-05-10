from django.db import models
class Covid(models.Model):
    Country=models.CharField(max_length=255)
    TotalConfirmed=models.CharField(max_length=255)
    TotalDeaths=models.CharField(max_length=255)
    TotalRecovered=models.CharField(max_length=255)
    Date=models.DateTimeField(auto_now_add=False) 
    
    
    def __str__(self):
        return self.country

