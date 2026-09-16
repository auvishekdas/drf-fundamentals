from django.db import models

# Create your models here.
class Aiquest(models.Model):
    student_name = models.CharField(max_length=30)
    class_name = models.CharField(max_length=15)
    seat = models.IntegerField()