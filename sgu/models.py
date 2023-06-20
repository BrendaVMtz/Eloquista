from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_teacher = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    intitution = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)
