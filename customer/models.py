from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 10)
    paswword = models.CharField(max_length = 20)

    class Meta():
        db_table = 'customer_tb'
    
    
    


