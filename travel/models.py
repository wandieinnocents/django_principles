from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=400)
    price = models.IntegerField()
    img = models.ImageField(upload_to='photos')
    description = models.TextField()
    offer = models.BooleanField(default=False)