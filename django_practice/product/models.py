from django.db import models

# Create your models here.
class User(models.Model):
    username = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=128)

#post method
#model User: username: email, password
#additional api: /register public api
#header: authorization: basic username:password  
#body: {"username":"","password"}
#response: "successfully register"
#/login 
#header: authorization: basic username:password 
#response:{"token"}
#middleware: checkbasicauth

class Product(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    supplier = models.CharField(max_length=255, default='supplier-1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name