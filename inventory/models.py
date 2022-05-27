from unicodedata import category
from django.db import models

# Create your models here.

# Inventory will have category and choice depend upon which is user demand
# inventory has one-to many relationship with items
class Categories(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name


class Items(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="categories")
    code =models.CharField(max_length=100,blank=True, null=True)
    name =models.CharField(max_length=200,blank=True, null=True)
    description = models.TextField()
    price = models.FloatField(default=0)
    discount = models.IntegerField()
    status = models.CharField(max_length=2, choices=(('1','In Stock'),('2','Out of Stock')), default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code + ' - ' + self.name

    