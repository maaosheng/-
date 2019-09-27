from django.db import models


# Create your models here.
class Pushier(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, unique=True)


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, unique=True)
    pushier = models.ForeignKey('Pushier', on_delete=models.CASCADE)


class Auther(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(null=False, max_length=30, unique=True)
    book = models.ManyToManyField(to=Book)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=36)
    cl = models.CharField(max_length=36,default=1)

