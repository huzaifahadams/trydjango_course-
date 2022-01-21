from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summury = models.CharField(max_length=100)
    discount = models.BooleanField(default=True)