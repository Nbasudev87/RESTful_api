from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    #comment=models.IntegerField(max_length=10)

    def __str__(self):
        return self.title
class Customer(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    brand = (
        ('1', 'HONDA'),
        ('2', 'BAJAJ'),
        ('3', 'TVS')
    )

    vehicle=models.CharField(max_length=1,choices=brand)
    ownername=models.OneToOneField(Customer,on_delete=models.CASCADE,related_name='vehicle')
    def __str__(self):
        return self.vehicle