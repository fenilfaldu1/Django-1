from django.db import models

# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=20)
    sold=models.BooleanField()


# class Standard(models.Model):
#     standard=models.CharField(max_length=12)

    # def __str__(self):
    #     return self.standard
    

class Student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    course=models.CharField(max_length=40)
    # standard=models.ForeignKey(Standard, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.name
    

