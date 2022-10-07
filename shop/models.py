from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class extendeduser(models.Model):
    mobile = models.CharField(max_length = 15)
    user = models.OneToOneField(User,on_delete=models.CASCADE) 

class State(models.Model):
    statename =models.CharField(max_length=30,unique=True)
    def __str__(self):
         return self.statename

class City(models.Model):
    statename = models.ForeignKey(State , on_delete=models.DO_NOTHING)
    cityname = models.CharField(max_length=30,unique=True)
    def __str__(self):
         return self.cityname

class Category(models.Model):
    catname = models.CharField(max_length=30,unique=True)
    catcommission = models.FloatField()
    def __str__(self):
         return self.catname

class subcat(models.Model):
    catname = models.ForeignKey(Category , on_delete=models.DO_NOTHING)
    subcatname = models.CharField(max_length=30,unique=True)  
    def __str__(self):
         return self.subcatname

class Product(models.Model):
    userid = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    prname = models.CharField(max_length=100)
    brandname = models.CharField(default=None, blank=True, null=True,max_length=30)
    catname = models.ForeignKey(Category , on_delete=models.DO_NOTHING)
    subcatname = models.ForeignKey(subcat , on_delete=models.DO_NOTHING)
    catname1 = models.CharField(default=None, blank=True, null=True,max_length=30)
    subcat1 = models.CharField(default=None, blank=True, null=True,max_length=30)
    img = models.ImageField(upload_to='pics')
    statename = models.ForeignKey(State , on_delete=models.DO_NOTHING)
    cityname = models.ForeignKey(City , on_delete=models.DO_NOTHING)
    statename1 = models.CharField(default=None, blank=True, null=True,max_length=30)
    cityname1 = models.CharField(default=None, blank=True, null=True,max_length=30)
    praddress = models.TextField()
    desc = models.TextField()
    yop = models.CharField(max_length=100)
    price = models.FloatField()
    payment= models.FloatField(default=None, blank=True, null=True)
    verifystatus = models.BooleanField(default=False)
    activestatus = models.BooleanField(default=True)
    accountno = models.CharField(default=None, blank=True, null=True,max_length=30)
    bankname = models.CharField(default=None, blank=True, null=True,max_length=30)
    ifsccode = models.CharField(default=None, blank=True, null=True,max_length=30)

    def __str__(self):
        return "{} : {}".format(str(self.id), self.prname)

class prverification(models.Model):
    verifier = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    verifydate = models.DateTimeField(default=None, blank=True, null=True)
    feedback = models.TextField(default=None, blank=True, null=True)
    prid = models.ForeignKey(Product , on_delete=models.DO_NOTHING)
    allotedstatus = models.BooleanField(default=True)

    def __str__(self):
        return self.id
