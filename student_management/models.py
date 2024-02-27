from django.db import models

class Standard(models.Model):
    std_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.std_name
    

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.CharField( max_length=50)
    standard=models.ForeignKey(Standard,on_delete=models.CASCADE)
    course = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    