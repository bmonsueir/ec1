#products
from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.db import models
from datetime import datetime

class Product(models.Model):
    name = models.CharField( max_length=255,)
    description = models.CharField( max_length=255, )
    amazon = models.CharField(max_length=255, )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.CharField( max_length=255,)
 
    
    
    def __str__(self):
        return self.name 
