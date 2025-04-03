from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=30)
    phone_num = models.CharField(max_length=11)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name
