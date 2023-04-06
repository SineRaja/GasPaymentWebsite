from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    usercnum = models.CharField(max_length=15, null=True)
    useradd = models.CharField(max_length=200, null=True)
    userplace = models.CharField(max_length=100,null=True)
    userst = models.CharField(max_length=100, null=True) 
    userregd = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Bill(models.Model):
    connection = models.ForeignKey(Customer,on_delete=models.CASCADE)
    billformonth = models.CharField(max_length=50, null=True)
    crdayele = models.CharField(max_length=50, null=True)
    prdayele = models.CharField(max_length=50, null=True)
    dayelectu = models.CharField(max_length=100, null=True)
    dayelechargeperunit = models.CharField(max_length=100, null=True)
    crnightele = models.CharField(max_length=50, null=True)
    prnightele = models.CharField(max_length=50, null=True)
    nighteletu = models.CharField(max_length=100, null=True)
    nightelechargeperunit = models.CharField(max_length=100, null=True)
    crgas = models.CharField(max_length=50, null=True)
    prgas = models.CharField(max_length=50, null=True)
    gastotalunit = models.CharField(max_length=100, null=True)
    gaschargeperunit = models.CharField(max_length=100, null=True)
    standingcharge = models.CharField(max_length=50, null=True)
    finalamount = models.CharField(max_length=100, null=True)
    duedate = models.DateField(null=True)
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.billformonth
