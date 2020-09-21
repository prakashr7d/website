from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
# from shop.models.cart import Cart


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Category(models.Model):
    category = models.CharField(max_length=100)

class Product(models.Model):
    RATING_DIR=(
        ('1','*'),
        ('2','**'),
        ('3','***'),
        ('4','****'),
        ('5','*****'),
    )
    product_name = models.CharField(max_length = 100)
    price = models.IntegerField()
    Category = models.ForeignKey('basicapp.Category', related_name = 'product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'product_image')
    description = models.TextField()
    specification = models.TextField(blank=True)
    availabe = models.BooleanField(default=False)
    rating = models.TextField(max_length = 10, choices=RATING_DIR)

# class Cart(models.Model):
#     Product = models.ForeignKey('basicapp.Product',related_name = 'cart',on_delete=models.CASCADE)
#     Customer = models.ForeignKey('basicapp.Customer',related_name = 'customer',on_delete=models.CASCADE)

class Comments(models.Model):
    Product = models.ForeignKey('basicapp.Product',related_name='comments', on_delete=models.CASCADE)
    Customer = models.ForeignKey('basicapp.Customer',related_name='User_comment', on_delete=models.CASCADE, blank = True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())

# class Order(models.Model):
#     name =  
#     address =
#     pincode
#     payment mode
#     Total amount



    
