from django.db import models

from products.models import Product

# Create your models here.

class Review(models.Model):
    item_review = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    review_text = models.CharField(max_length=2000)


# class Product(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     picture = models.CharField(max_length=2000, default='')
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     inventory_quantity = models.IntegerField()
####################
# •	Add a new app based around a Review model with full CRUD functionality.
# •	Review should have a many to one relationship with Products (One Product, Many Reviews)
# •	When Adding a new Review, you will need to include the FK of the Product it is a Review of.
# •	You should also add a new endpoint that will be a little different from standard CRUD:
# •	Create an endpoint which will allow you to pass in a Product’s id and it will respond with a collection of all the Reviews associated with that Product.
# This can be using class based or function based views, your choice!
