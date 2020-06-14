from django.db import models
from _datetime import datetime
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/")
    manufactured_by=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="photos/%Y/%m/%d/")
    price=models.DecimalField(max_digits=4,decimal_places=2)
    qty_sold=models.IntegerField()
    qty_available=models.IntegerField()
    is_sale=models.BooleanField(default=False)
    is_bestSeller=models.BooleanField(default=False)
    is_newArrival=models.BooleanField(default=False)
    description=models.TextField(blank=True)
    is_published=models.BooleanField(default=True)
    rating=models.IntegerField()
    stars=GenericRelation(Rating,related_query_name='product')
    product_date=models.DateTimeField(default=datetime.now)
    is_offer=models.BooleanField(default=False)
    offer_price=models.DecimalField(max_digits=4,decimal_places=2,blank=True)
    def __str__(self):
        return self.name
    