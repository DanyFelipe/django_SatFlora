from django.db import models
from django.contrib.auth.models import User

class City(models.Model):
    idCity = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    idProject = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    users = models.ManyToManyField(User, related_name='user_project') 

    def __str__(self):
        return self.name
    
class Product(models.Model):
    idProduct = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    derived = models.BooleanField(default=False)
    idProject = models.ForeignKey("Project", on_delete=models.SET_NULL, null=True)  
    idImage = models.ForeignKey("Image", on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        return self.name 
    
class ImageType(models.Model):
    idImageType = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    visible = models.BinaryField()

    def __str__(self):
        return self.name    
    
class Image(models.Model):
    idImage = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.BinaryField()  
    idImageType = models.ForeignKey(ImageType, on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        return self.name        
    
class Coordinate(models.Model):
    idCoordinate = models.AutoField(primary_key=True)
    geometry = models.JSONField()
    properties = models.JSONField()
    type = models.CharField(max_length=100)  
    idImage = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        return f"Coordinate {self.idCoordinate} for Image {self.idImage}"    
    
class Dictionary(models.Model):
    idDictionary = models.AutoField(primary_key=True)
    label = models.IntegerField()
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Dictionary Entry {self.idDictionary}: {self.label}"    
