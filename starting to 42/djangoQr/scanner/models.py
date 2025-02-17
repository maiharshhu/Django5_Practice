from django.db import models

# Create your models here.
class QRcode(models.Model):
    data = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.data} - {self.mobile_number}"