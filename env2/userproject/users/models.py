from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# from django.core.validators import RegexValidator

# Create your models here.

# cerate AbstractUser model
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # phone = PhoneNumberField(region='IN')
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
class Sector(models.Model):
    sector_name = models.CharField(max_length=100, default="Golakganj")
    def __str__(self):
        return f"{self.sector_name}"

class Worker(models.Model):
    sector = models.ForeignKey(Sector, related_name='worker', on_delete=models.CASCADE)
    AWC_Code = models.IntegerField()
    AWC_Name = models.CharField(max_length=100)
    AWW_Name = models.CharField(max_length=100)
    AWW_Phone = PhoneNumberField(region='IN')
        # max_length=13,
        # validators=[
        #     RegexValidator(
        #         regex=r'^\+91\d{10}$',
        #         message="Phone number must be entered in the format: '+911234567890'. Up to 13 digits allowed."
        #     )
        # ])
    AWH_Name = models.CharField(max_length=100)
    AWH_Phone = PhoneNumberField(region='IN')
    AWC_Address = models.TextField()

    GOVTBUILDING = 'Govt Building'
    PRIVATEBUILDING = 'Private Building'

    BUILDING_TYPE_CHOICES = [
        (GOVTBUILDING, GOVTBUILDING),
        (PRIVATEBUILDING, PRIVATEBUILDING),
         ]
    
    Building_Type = models.CharField(
        max_length=20,
        choices=BUILDING_TYPE_CHOICES,)
        
    AWC_Image = models.ImageField(upload_to='AWC_images/', blank=True, null=True)   
    Drinking_Water_Facility = models.BooleanField(default=False) 
    Toilet_Facility = models.BooleanField(default=False)
    Electricity_Avaiable = models.BooleanField(default=False)
    Kitchen_Garden_Available = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sector}:{self.AWW_Name}"