from django.db import models

# Create your models here.
class layout(models.Model):
   Product = models.CharField(max_length=50)
   Description = models.TextField(max_length=250)
   Price = models.IntegerField()
   ProductImage = models.ImageField(null=True,blank=True)
   Offer = models.BooleanField(default=False)

class Contact(models.Model):
   Name = models.CharField(max_length=50)
   Email = models.EmailField(blank=False)
   Phone = models.IntegerField(blank=False)
   Description = models.TextField(blank=True)

class Products(models.Model):
   Name = models.CharField(max_length=50)
   Description = models.TextField(max_length=250)
   Price = models.IntegerField()
   ProdImage = models.ImageField(null= True, blank = True)
   Offer = models.BooleanField(default=False)

