from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import IntegerField
from django.db.models.fields.related import ForeignKey, ManyToManyField
from django.utils import timezone
# Create your models here.


class Recipe(models.Model):
    name = models.CharField(max_length=255, default='')
    photo = models.ImageField(upload_to='recipes/')
    recipe_ingrident = models.ManyToManyField('Ingrident')
    recipe_type = models.ForeignKey("RecipeType", blank=True , null= True  ,on_delete=models.SET_NULL)
    duration = models.IntegerField(null = True , blank= True)
    time_of_create = models.DateField(default = timezone.now)

    
    recipe_description = models.TextField(default = '')

    def __str__(self):
        return f" {self.name} {self.id} "
    

class Ingrident(models.Model):
    name = models.CharField(max_length=255)
    ingrident_type = models.ForeignKey('Species', on_delete= models.SET_NULL , related_name = "ingrident_species", null = True , blank = True)
    calories = models.IntegerField(null = True , blank = True)

    def __str__(self):
        return f" {self.name} {self.id} "

class Species(models.Model):
    name =  models.CharField(max_length=255, default='')

    def __str__(self):
        return f" {self.name} {self.id} "



class RecipeType(models.Model):
    name =  models.CharField(max_length=255, default='')

    def __str__(self):
        return f" {self.name} {self.id} "


class Amount(models.Model):
    number = models.FloatField(null = True , blank= True)

    def __str__(self):
        return f" {self.name} {self.id} "

class Test(models.Model):
    recipe = models.ForeignKey(Recipe , related_name = "test_amount" , on_delete=models.SET_NULL , null=True , blank = True)
    ingrident = models.ForeignKey(Ingrident, on_delete=models.SET_NULL , null=True , blank = True)
    amount = models.IntegerField(null = True , blank= True)

