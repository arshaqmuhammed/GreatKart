from django.db import models

# Create your models here.
class Seller(models.Model):
    firstname = models.CharField(max_length = 30)
    lastname = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    gender = models.CharField(max_length = 10)
    city = models.CharField(max_length = 20)
    country = models.CharField(max_length = 10)
    paswword = models.CharField(max_length = 20)
    picture = models.ImageField(upload_to = 'seller/')
    accnumber = models.CharField(max_length = 30)
    loginid = models.CharField(max_length = 30)
    company_name = models.CharField(max_length = 20 , default = '')
    bank_name = models.CharField(max_length = 20 , default = '') 
    bank_branch = models.CharField(max_length = 20 , default = '')
    ifsc = models.CharField(max_length = 30 , default = '')
    status = models.CharField(max_length = 50, default = 'pending')

    class Meta():
        db_table = 'seller_tb'
    