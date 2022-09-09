from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

GENDER = [
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
]

class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name



BloodGroup =[
    ('A+','A+'),
    ('A-','A-'),
    ('O+','O+'),
    ('O-','O-')
]
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(help_text="yyyy-mm-dd")
    phone = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    blood_group = models.CharField(choices=BloodGroup,max_length=5)
    gender = models.CharField(choices=GENDER, max_length=10)




    def __str__(self):
        return self.user.username
