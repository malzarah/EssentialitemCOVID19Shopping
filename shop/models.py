from datetime import timezone

from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin,UserManager


# Create your models here.


# class Person(AbstractBaseUser, PermissionsMixin):
#     firstName = models.CharField(max_length=100)
#     lastName = models.CharField(max_length=100)
#     objects = UserManager()
#     def get_fullName(self):
#         return self.firstName + self.lastName
#
#     @property
#     def fullName(self):
#         return self.get_fullName()


class item(models.Model):
    item_ID=models.AutoField(primary_key=True)
    itemName= models.CharField(max_length=100,default="none")
    itemDescription= models.CharField(max_length=200, default="")
    itemEssentialFlag=models.BooleanField(default="True")
    itemQty=models.IntegerField(default=1)
    created=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    # user=models.ForeignKey(Person,on_delete=models.CASCADE)



    def __unicode__(self):
        return '%s' % self.itemName


class archive(models.Model):
    archive_ID= models.AutoField(primary_key=True)
    item= models.ForeignKey(item, on_delete=models.CASCADE)
    itemName=models.CharField(max_length=200)
    itemDescription= models.CharField(max_length=500)
    itemEssentialFlag=models.BooleanField(default=True)
    itemQty=models.IntegerField(default=0)

class usage(models.Model):
    usage_ID=models.AutoField(primary_key=True)
    usagePerc=models.FloatField(default=0.00)
    item= models.ForeignKey(item,on_delete=models.CASCADE)

class store(models.Model):
    store_ID=models.AutoField(primary_key=True)
    store_NAME=models.CharField(max_length=500)
    item=models.ForeignKey(item,on_delete=models.CASCADE)