from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    father_name = models.CharField(max_length=100)
    # dob = models.DateField(max_length=8)

    def __str__(self):
        return f"{self.name}"
    

class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.category_name}"

class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    Book_title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.category, self.Book_title }"
    
# Create a new model for student details
class Admition(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    dob = models.DateField()
    email = models.EmailField(max_length=70, blank=True, unique=True)
    phone = PhoneNumberField()
    address = models.TextField()
    def __str__(self):
        return f"{self.name}"