from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    age = models.IntegerField()

    def __str__(self):
        return self.username

class BitcoinInfo(models.Model):
    price = models.IntegerField()
    timestamp = models.CharField(max_length=100)
    def __str__(self):
        return self.price