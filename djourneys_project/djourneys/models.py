from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    continent = models.CharField(max_length=30)
    state = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Attraction(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='attraction')
    name = models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name
    
class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='review')
    star_rating = models.IntegerField(default=3,
                                      validators=[
                                          MinValueValidator(1),
                                          MaxValueValidator(5)
                                      ])
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title
