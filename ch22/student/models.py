from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=254)
    city = models.CharField(max_length=70)
    roll = models.IntegerField()
    state = models.CharField(max_length=70)
    comment = models.CharField(max_length=70, default="nothing")
