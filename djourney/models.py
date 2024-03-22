from django.db import models

# Create your models here.

class Cities(models.Model):
    name = models.CharField(max_length=100)
    population = models.CharField(max_length=100)
    photo_url = models.TextField()

class Attractions(models.Model):
    name = models.CharField(max_length=100)
    ratings = models.CharField(max_length=100)
    photo_url = models.TextField()

class Reviews(models.Model):
    name = models.CharField(max_length=100)
    resident = models.BooleanField()
    review = models.CharField(max_length=300)