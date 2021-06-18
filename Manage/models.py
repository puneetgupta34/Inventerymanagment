from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, CharField

# Create your models here.


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(TimeStampedModel):
    Product_id = models.CharField(max_length=50, unique=True)
    Quantity = models.IntegerField()
    reserved_quantity = models.IntegerField()


class Location(TimeStampedModel):
    Location_id = models.CharField(max_length=50)
    Address = models.CharField(max_length=100)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class ProductMovement(TimeStampedModel):
    Movement_id = models.IntegerField(unique=True)
    from_location = models.ForeignKey(
        Location, related_name="address",  on_delete=models.CASCADE)
    to_location = models.ForeignKey(Location,  on_delete=models.CASCADE)
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
