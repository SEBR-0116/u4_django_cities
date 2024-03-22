from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    population = models.IntegerField()

    def __str__(self):
        return self.name


class Attraction(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, related_name='attraction')

    def __str__(self):
        return self.name
    

class Review(models.Model):
    attraction = models.ForeignKey(Attraction, on_delete=models.CASCADE, related_name='review')
    username = models.CharField(max_length=100)
    review = models.TextField()
    ratings = models.IntegerField(default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])

    def __str__(self):
        return self.review