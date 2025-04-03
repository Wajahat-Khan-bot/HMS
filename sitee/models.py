from django.db import models
from customer.models import Customer


class Sitee(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    phone_num= models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)

    def __str__(self):
        return self.name