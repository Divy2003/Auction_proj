from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bidder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    
    def __str__(self):
        return self.user.username

class Auction_User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=100,null=True)
    contact = models.CharField(max_length=10,null=True)
    image = models.FileField(null=True)
    
    def __str__(self):
        return self.user.username

class Status(models.Model):
    status = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.status
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('tractor', 'Tractor'),
        ('bike-p', 'Bike-parts'),
        ('car-p', 'Car-parts'),
        ('tractor-p', 'Tractor-parts'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True)

    temp = models.IntegerField(null=True)
    status = models.CharField(max_length=30, default='pending')
    name = models.CharField(max_length=100,null=True)
    min_price = models.IntegerField(null=True)
    images = models.FileField(null=True)
    auction_date = models.DateField(null=True)  
    auction_time = models.TimeField(null=True) 

    def __str__(self):
        return self.name

class Aucted_Product(models.Model):
    winner = models.CharField(max_length=100,null=True)
    user = models.ForeignKey(Auction_User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.user.username+ " " + self.product.name     
class Payment(models.Model):
    pay = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.pay


    
class Participant(models.Model):
   
    new_price = models.IntegerField(null=True)
    
    user = models.ForeignKey(Bidder,on_delete=models.CASCADE,null=True)
    aucted_product = models.ForeignKey(Aucted_Product,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)     
    payment = models.CharField(max_length=100, null=True)  # Changed to CharField
    result = models.CharField(max_length=100, null=True)   # Changed to CharField



    
class Send_Feedback(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    message1 = models.TextField(null=True)
    date = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.profile.username  