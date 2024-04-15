from django.db import models

# Create your models here.

class customer(models.Model):
    cname=models.CharField(max_length=20)
    cmob=models.IntegerField()
    def __str__(self) -> str:
        return self.cname

class product(models.Model):
    pname=models.CharField(max_length=20)
    pcost=models.IntegerField()
    cus=models.ForeignKey(customer,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.pname