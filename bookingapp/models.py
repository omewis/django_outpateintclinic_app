from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.
class doctor(models.Model):
    name= models.CharField(max_length=50,null=True)
    phone = models.IntegerField()
    speciality = models.CharField(max_length=30,null=True )
    start_time = models.TimeField() 
    end_time = models.TimeField( ) 
    attendance_day = models.CharField(max_length=20,null=True )

    def __str__(self) -> str:
        return self.speciality+ ": " + self.name

class Booking(models.Model):
    first_name = models.CharField(max_length=30,null=True )
    last_name = models.CharField(max_length=30,null=True )
    phone      = models.IntegerField(null=True )
    speciality = models.ForeignKey(doctor,null=True ,on_delete=models.CASCADE )
    available_time = models.CharField(max_length=20,null=True ) 

    def __str__(self) -> str:
        return self.first_name
    

    

class clinic(models.Model):
    name= models.CharField(max_length=50,null=True)
    def __str__(self) -> str:
        return self.name

class num_of_building(models.Model):
    num = models.CharField(max_length=50,null=True)
    information = models.ForeignKey(clinic,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.num


class clininfo(models.Model):
    information=models.ForeignKey(clinic,related_name='info',on_delete=models.CASCADE,null=True)
    doctor_name= models.ForeignKey(doctor,null=True,on_delete=models.CASCADE)
    num_of_bulding=models.ForeignKey(num_of_building,null=True,on_delete=models.CASCADE)
   



    
    

