from django.db import models

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=70)
    roll = models.IntegerField()
    email = models.EmailField(max_length=255)
    city = models.CharField(max_length=70)

    # def __str__(self):
    #     # return self.name
    #     return str(self.roll)
# note:- __str__ method only works with string data if you want to work with integer data then need to type cast str(self.id)


class Result(models.Model):
    stu_class = models.CharField(max_length=70)
    marks = models.IntegerField()

    # def __str__(self):
    #     return str(self.stu_class)
