from django.db import models

class PaginationModel(models.Model):
    idno=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True)
    salary=models.FloatField()
