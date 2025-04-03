from django.db import models
from client.models import Client

class Customer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

