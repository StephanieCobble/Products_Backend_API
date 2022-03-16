
from django.db import models
from products.models import Product

# Create your models here.

class Review(models.Model):
    item_name = models.CharField(max_length=255, default='Review')
    review_text = models.TextField()
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)


####################
# •	Add a new app based around a Review model with full CRUD functionality.
# •	Review should have a many to one relationship with Products (One Product, Many Reviews)
# •	When Adding a new Review, you will need to include the FK of the Product it is a Review of.
# •	You should also add a new endpoint that will be a little different from standard CRUD:
# •	Create an endpoint which will allow you to pass in a Product’s id and it will respond with a collection of all the Reviews associated with that Product.
# This can be using class based or function based views, your choice!
#################
#django many to one