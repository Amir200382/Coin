from django.db import models

class CoinWarning(models.Model):
    name = models.CharField(max_length=100)  
    price = models.FloatField()              
    condition = models.IntegerField()        
    email = models.EmailField()              
    last_notified_price = models.FloatField(null=True, blank=True)  

    def __str__(self):
        return f"{self.name} - {self.price} ({self.condition})"
