from django.db import models

# Create your models here.

class license(models.Model):
	content = models.TextField()

class fname(models.Model):
	content = models.TextField()

class lname(models.Model):
	content = models.TextField()

class mbutton(models.Model):
	state = models.BooleanField(default= False)

class driving(models.Model):
	speed = models.IntegerField()
