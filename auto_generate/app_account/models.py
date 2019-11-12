from django.db import models

class Accounts(models.Model):
    acno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=20)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    balance=models.DecimalField(max_digits=10,decimal_places=2)
    picture=models.ImageField(upload_to='acc_images',default=False)