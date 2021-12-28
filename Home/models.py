from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Employee(models.Model):
    name= CharField(max_length=100)
    dep= CharField(max_length=100)
    salary= IntegerField()
    phone=IntegerField()
     

    def __str__(self):
        return self.name


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>














# class Category(models.Model):
#     category_name= models.CharField(max_length=100)

# class Book(models.Model):
#     category= ForeignKey(Category, on_delete=models.CASCADE)
#     book_title= models.CharField(max_length=100)

# class Student(models.Model):
#     name= CharField(max_length=100)
#     std= IntegerField()




