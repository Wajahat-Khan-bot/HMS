from django.db import models
from sitee.models import Sitee

class Asset (models.Model):
    name = models.CharField(max_length=50)
    phone_num = models.IntegerField()
    address = models.CharField(max_length=50)
    sitee = models.ForeignKey(Sitee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    