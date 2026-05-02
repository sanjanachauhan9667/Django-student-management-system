from django.db import models

# Create your models here.
class StudentRecord(models.Model):

    Gender_Choices = [
        ('M','Male'),
        ('F','female'),
        ('O','Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices= Gender_Choices)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name