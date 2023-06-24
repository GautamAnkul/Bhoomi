from django.db import models
from django.db.models.fields import CommaSeparatedIntegerField

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    state = models.ForeignKey(to=State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)



    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True, unique=True)


    def __str__(self) -> str:
        return self.name


class Property(models.Model):
    state = models.ForeignKey(to=State, on_delete=models.CASCADE)
    city = models.ForeignKey(to=City,on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.CharField(max_length=255,blank=True, null=False)
    longitude = models.CharField(max_length=255,blank=True, null=False)



    def __str__(self) -> str:
        return self.name

class ContactUs(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=50,blank=True ,null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.username
