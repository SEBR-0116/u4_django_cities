from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    int_airports = ArrayField(models.CharField(max_length=100))

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attractions')
    name = models.CharField(max_length=100)
    neighbourhood = models.CharField(max_length=100)
    free = models.BooleanField()
    type = models.CharField(max_length=100)
    price_adult = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
    
class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.CharField(max_length=20)
    review = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.reviewer