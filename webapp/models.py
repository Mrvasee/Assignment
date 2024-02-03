from django.db import models

class Intern_Detail(models.Model):
    Full_name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Phone_No=models.CharField(max_length=10)
    Degree=models.CharField(max_length=100)
    Field=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    City=models.CharField(max_length=50)
    Pincode=models.IntegerField()
    State=models.CharField(max_length=50)
    def __str__(self):
        return self.Full_name 
    
# Create your models here.
