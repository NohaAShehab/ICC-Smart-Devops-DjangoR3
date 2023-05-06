from django.db import models

# Create your models here.

""" model is a class represent table structure """

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30, null=True)
    grade = models.IntegerField(default=0, null=True, blank=True)
    email = models.EmailField( null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,  null=True)
    updated_at = models.DateTimeField(auto_now=True,  null=True)


    def __str__(self):
        return self.first_name
