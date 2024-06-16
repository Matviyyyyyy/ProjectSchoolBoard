from django.db import models

# Create your models here.

class Subject(models.Model):
    title = models.CharField(max_length=300)

class Teacher(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)

class Class(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    email = models.EmailField()
    class_id = models.ForeignKey(Class, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
